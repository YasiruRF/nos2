"""Test script for AST Builder.

This script tests the ASTBuilder class to ensure it can properly construct
AST nodes from various source constructs.
"""

import sys
sys.path.insert(0, 'D:/Praxis/NOS')

from flowlang.ast.builder import ASTBuilder
from flowlang.ast import nodes


def test_source_location():
    """Test source location creation."""
    builder = ASTBuilder("test.flow")
    loc = builder._loc(None)
    assert loc.line == 0
    assert loc.column == 0
    assert loc.file == "test.flow"
    print("  Source location: OK")


def test_strip_quotes():
    """Test string quote stripping."""
    builder = ASTBuilder()
    assert builder._strip_quotes('"hello"') == "hello"
    assert builder._strip_quotes("'hello'") == "hello"
    assert builder._strip_quotes('hello') == "hello"
    assert builder._strip_quotes('"') == '"'
    print("  Quote stripping: OK")


def test_primitive_type():
    """Test primitive type creation."""
    builder = ASTBuilder("test.flow")

    # Create a mock context
    class MockCtx:
        def __init__(self, text):
            self._text = text
            self.start = type('obj', (object,), {'line': 1, 'column': 0})()

        def getText(self):
            return self._text

    ctx_int = MockCtx("int")
    result = builder.visit_PrimitiveType(ctx_int)
    assert isinstance(result, nodes.PrimitiveType)
    assert result.kind == nodes.PrimitiveTypeKind.INT

    ctx_string = MockCtx("string")
    result = builder.visit_PrimitiveType(ctx_string)
    assert result.kind == nodes.PrimitiveTypeKind.STRING

    print("  Primitive types: OK")


def test_qualified_identifier():
    """Test qualified identifier parsing."""
    builder = ASTBuilder("test.flow")

    # Create mock context with identifier list
    class MockId:
        def __init__(self, text):
            self._text = text
        def getText(self):
            return self._text

    class MockCtx:
        def identifier(self):
            return [MockId("sensor_msgs"), MockId("LaserScan")]

    result = builder.visit_QualifiedIdentifier(MockCtx())
    assert result == "sensor_msgs::LaserScan"
    print("  Qualified identifier: OK")


def test_literal_expression():
    """Test literal expression creation."""
    builder = ASTBuilder("test.flow")

    class MockCtx:
        def __init__(self):
            self.start = type('obj', (object,), {'line': 1, 'column': 0})()

    # Test various literal types
    class IntLiteral(MockCtx):
        def INT_LITERAL(self):
            return type('obj', (object,), {'getText': lambda *args: "42"})()

    class StringLiteral(MockCtx):
        def STRING_LITERAL(self):
            return type('obj', (object,), {'getText': lambda *args: '"hello"'})()
    class TrueLiteral(MockCtx):
        def TRUE(self):
            return True
        def getText(self):
            return "true"

    result = builder.visit_literal(IntLiteral())
    assert isinstance(result, nodes.LiteralExpression)
    assert result.value == 42
    assert result.literal_type == "int"

    result = builder.visit_literal(StringLiteral())
    assert result.value == "hello"
    assert result.literal_type == "string"

    result = builder.visit_literal(TrueLiteral())
    assert result.value == True
    assert result.literal_type == "bool"

    print("  Literal expressions: OK")


def test_file_node():
    """Test File node creation."""
    builder = ASTBuilder("test.flow")

    # Create a file with package declaration
    loc = nodes.SourceLocation(1, 0, "test.flow")
    pkg = nodes.PackageDecl(location=loc, name="test_pkg", version="1.0.0")
    imp = nodes.ImportDecl(location=loc, qualified_name="std_msgs::Header")
    node_decl = nodes.NodeDecl(location=loc, name="TestNode")

    file_node = nodes.File(
        location=loc,
        package=pkg,
        imports=[imp],
        declarations=[node_decl]
    )

    assert file_node.package.name == "test_pkg"
    assert len(file_node.imports) == 1
    assert len(file_node.declarations) == 1
    assert file_node.declarations[0].name == "TestNode"

    print("  File node construction: OK")


def test_parameter_decl():
    """Test parameter declaration."""
    builder = ASTBuilder("test.flow")
    loc = nodes.SourceLocation(1, 0, "test.flow")

    param = nodes.ParameterDecl(
        location=loc,
        name="frame_id",
        type=nodes.PrimitiveType(location=loc, kind=nodes.PrimitiveTypeKind.STRING),
        default_value=nodes.LiteralExpression(location=loc, value="laser", literal_type="string"),
        constraints=[
            nodes.Constraint(location=loc, name="required", arguments=[])
        ]
    )

    assert param.name == "frame_id"
    assert param.type.kind == nodes.PrimitiveTypeKind.STRING
    assert param.default_value.value == "laser"
    assert len(param.constraints) == 1
    assert param.constraints[0].name == "required"

    print("  Parameter declaration: OK")


def test_subscription_decl():
    """Test subscription declaration."""
    builder = ASTBuilder("test.flow")
    loc = nodes.SourceLocation(1, 0, "test.flow")

    msg_type = nodes.QualifiedType(location=loc, package="sensor_msgs", name="LaserScan")
    topic = nodes.LiteralExpression(location=loc, value="/scan", literal_type="string")

    sub = nodes.SubscriptionDecl(
        location=loc,
        name="scan",
        message_type=msg_type,
        topic=topic,
        constraints=[
            nodes.Constraint(location=loc, name="queue_size", arguments=[
                nodes.LiteralExpression(location=loc, value=10, literal_type="int")
            ])
        ]
    )

    assert sub.name == "scan"
    assert sub.message_type.package == "sensor_msgs"
    assert sub.message_type.name == "LaserScan"
    assert sub.topic.value == "/scan"
    assert len(sub.constraints) == 1

    print("  Subscription declaration: OK")


def test_launch_decl():
    """Test launch declaration."""
    builder = ASTBuilder("test.flow")
    loc = nodes.SourceLocation(1, 0, "test.flow")

    arg = nodes.ArgumentDecl(
        location=loc,
        name="use_simulation",
        type=nodes.PrimitiveType(location=loc, kind=nodes.PrimitiveTypeKind.BOOL),
        default_value=nodes.LiteralExpression(location=loc, value=False, literal_type="bool")
    )

    node_instance = nodes.NodeInstance(
        location=loc,
        name="lidar",
        node_type="LidarProcessor",
        parameters={"port": nodes.LiteralExpression(location=loc, value="/dev/ttyUSB0", literal_type="string")}
    )

    group = nodes.GroupDecl(
        location=loc,
        name="sensors",
        namespace=nodes.LiteralExpression(location=loc, value="sensors", literal_type="string"),
        nodes=[node_instance]
    )

    launch = nodes.LaunchDecl(
        location=loc,
        name="NavigationStack",
        arguments=[arg],
        groups=[group],
        containers=[],
        includes=[],
        lifecycle_manager=None,
        events=[]
    )

    assert launch.name == "NavigationStack"
    assert len(launch.arguments) == 1
    assert launch.arguments[0].name == "use_simulation"
    assert len(launch.groups) == 1
    assert launch.groups[0].name == "sensors"
    assert len(launch.groups[0].nodes) == 1

    print("  Launch declaration: OK")


def test_interface_decl():
    """Test interface declaration."""
    builder = ASTBuilder("test.flow")
    loc = nodes.SourceLocation(1, 0, "test.flow")

    header_field = nodes.FieldDecl(
        location=loc,
        name="header",
        type=nodes.QualifiedType(location=loc, package="std_msgs", name="Header")
    )

    message = nodes.MessageDecl(
        location=loc,
        name="SensorFusionOutput",
        id=1,
        fields=[header_field]
    )

    iface = nodes.InterfaceDecl(
        location=loc,
        declarations=[message]
    )

    assert len(iface.declarations) == 1
    assert iface.declarations[0].name == "SensorFusionOutput"
    assert len(iface.declarations[0].fields) == 1

    print("  Interface declaration: OK")


def test_callback_decl():
    """Test callback declaration."""
    builder = ASTBuilder("test.flow")
    loc = nodes.SourceLocation(1, 0, "test.flow")

    callback = nodes.CallbackDecl(
        location=loc,
        event="on_init",
        parameters=[],
        body="# Initialize node"
    )

    assert callback.event == "on_init"
    assert callback.body == "# Initialize node"

    callback2 = nodes.CallbackDecl(
        location=loc,
        event="on_scan_received",
        parameters=[
            nodes.ParameterDecl(
                location=loc,
                name="msg",
                type=nodes.QualifiedType(location=loc, package="sensor_msgs", name="LaserScan")
            )
        ],
        body="process_scan(msg)"
    )

    assert callback2.event == "on_scan_received"
    assert len(callback2.parameters) == 1
    assert callback2.parameters[0].name == "msg"

    print("  Callback declaration: OK")


def test_visitor_methods_exist():
    """Test that all required visitor methods exist."""
    builder = ASTBuilder()

    required_methods = [
        'visit_FlowFile',
        'visit_PackageDecl',
        'visit_ImportDecl',
        'visit_NodeDecl',
        'visit_ParameterDecl',
        'visit_SubscriptionDecl',
        'visit_PublicationDecl',
        'visit_ServiceDecl',
        'visit_ActionDecl',
        'visit_CallbackDecl',
        'visit_ComponentDecl',
        'visit_LaunchDecl',
        'visit_ArgumentDecl',
        'visit_GroupDecl',
        'visit_NodeInstance',
        'visit_ContainerDecl',
        'visit_IncludeDecl',
        'visit_LifecycleManagerDecl',
        'visit_TransitionDecl',
        'visit_LaunchEventDecl',
        'visit_EventAction',
        'visit_InterfaceDecl',
        'visit_MessageDecl',
        'visit_ServiceDecl_interface',
        'visit_ActionDecl_interface',
        'visit_Constraint',
        'visit_Expression',
        'visit_Literal',
        'visit_PrimitiveType',
        'visit_QualifiedIdentifier',
    ]

    missing = []
    for method in required_methods:
        if not hasattr(builder, method):
            missing.append(method)

    if missing:
        print(f"  Missing methods: {missing}")
        raise AssertionError(f"Missing {len(missing)} visitor methods")

    print(f"  All {len(required_methods)} required visitor methods exist: OK")


def run_all_tests():
    """Run all tests."""
    print("=" * 60)
    print("AST Builder Test Suite")
    print("=" * 60)

    tests = [
        ("Source Location", test_source_location),
        ("Quote Stripping", test_strip_quotes),
        ("Primitive Types", test_primitive_type),
        ("Qualified Identifier", test_qualified_identifier),
        ("Literal Expressions", test_literal_expression),
        ("File Node", test_file_node),
        ("Parameter Declaration", test_parameter_decl),
        ("Subscription Declaration", test_subscription_decl),
        ("Launch Declaration", test_launch_decl),
        ("Interface Declaration", test_interface_decl),
        ("Callback Declaration", test_callback_decl),
        ("Visitor Methods", test_visitor_methods_exist),
    ]

    passed = 0
    failed = 0

    for name, test_func in tests:
        try:
            test_func()
            passed += 1
        except Exception as e:
            print(f"  FAILED: {e}")
            failed += 1

    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
