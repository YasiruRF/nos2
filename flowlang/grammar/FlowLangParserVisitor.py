# Generated from flowlang/grammar/FlowLangParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FlowLangParser import FlowLangParser
else:
    from FlowLangParser import FlowLangParser

# This class defines a complete generic visitor for a parse tree produced by FlowLangParser.

class FlowLangParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FlowLangParser#flowFile.
    def visitFlowFile(self, ctx:FlowLangParser.FlowFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#packageDecl.
    def visitPackageDecl(self, ctx:FlowLangParser.PackageDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#version.
    def visitVersion(self, ctx:FlowLangParser.VersionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#depends.
    def visitDepends(self, ctx:FlowLangParser.DependsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#importDecl.
    def visitImportDecl(self, ctx:FlowLangParser.ImportDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#nodeDecl.
    def visitNodeDecl(self, ctx:FlowLangParser.NodeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#nodeBody.
    def visitNodeBody(self, ctx:FlowLangParser.NodeBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#parameterBlock.
    def visitParameterBlock(self, ctx:FlowLangParser.ParameterBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#parameterDecl.
    def visitParameterDecl(self, ctx:FlowLangParser.ParameterDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#constraint.
    def visitConstraint(self, ctx:FlowLangParser.ConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#typeSpec.
    def visitTypeSpec(self, ctx:FlowLangParser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#primitiveType.
    def visitPrimitiveType(self, ctx:FlowLangParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#fieldDecl.
    def visitFieldDecl(self, ctx:FlowLangParser.FieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#subscriptionBlock.
    def visitSubscriptionBlock(self, ctx:FlowLangParser.SubscriptionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#subscriptionDecl.
    def visitSubscriptionDecl(self, ctx:FlowLangParser.SubscriptionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#publicationBlock.
    def visitPublicationBlock(self, ctx:FlowLangParser.PublicationBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#publicationDecl.
    def visitPublicationDecl(self, ctx:FlowLangParser.PublicationDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#serviceBlock.
    def visitServiceBlock(self, ctx:FlowLangParser.ServiceBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#serviceDecl.
    def visitServiceDecl(self, ctx:FlowLangParser.ServiceDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#actionBlock.
    def visitActionBlock(self, ctx:FlowLangParser.ActionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#actionDecl.
    def visitActionDecl(self, ctx:FlowLangParser.ActionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#lifecycleDecl.
    def visitLifecycleDecl(self, ctx:FlowLangParser.LifecycleDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#componentBlock.
    def visitComponentBlock(self, ctx:FlowLangParser.ComponentBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#componentDecl.
    def visitComponentDecl(self, ctx:FlowLangParser.ComponentDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#parameterOverride.
    def visitParameterOverride(self, ctx:FlowLangParser.ParameterOverrideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#callbackDecl.
    def visitCallbackDecl(self, ctx:FlowLangParser.CallbackDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#pythonCode.
    def visitPythonCode(self, ctx:FlowLangParser.PythonCodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#launchDecl.
    def visitLaunchDecl(self, ctx:FlowLangParser.LaunchDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#launchBody.
    def visitLaunchBody(self, ctx:FlowLangParser.LaunchBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#argumentBlock.
    def visitArgumentBlock(self, ctx:FlowLangParser.ArgumentBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#argumentDecl.
    def visitArgumentDecl(self, ctx:FlowLangParser.ArgumentDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#groupDecl.
    def visitGroupDecl(self, ctx:FlowLangParser.GroupDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#nodeInstance.
    def visitNodeInstance(self, ctx:FlowLangParser.NodeInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#nodeConfig.
    def visitNodeConfig(self, ctx:FlowLangParser.NodeConfigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#remapDecl.
    def visitRemapDecl(self, ctx:FlowLangParser.RemapDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#containerDecl.
    def visitContainerDecl(self, ctx:FlowLangParser.ContainerDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#componentInstance.
    def visitComponentInstance(self, ctx:FlowLangParser.ComponentInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#includeDecl.
    def visitIncludeDecl(self, ctx:FlowLangParser.IncludeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#includeArgs.
    def visitIncludeArgs(self, ctx:FlowLangParser.IncludeArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#namedArgument.
    def visitNamedArgument(self, ctx:FlowLangParser.NamedArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#lifecycleManagerDecl.
    def visitLifecycleManagerDecl(self, ctx:FlowLangParser.LifecycleManagerDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#managesBlock.
    def visitManagesBlock(self, ctx:FlowLangParser.ManagesBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#transitionBlock.
    def visitTransitionBlock(self, ctx:FlowLangParser.TransitionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#transitionDecl.
    def visitTransitionDecl(self, ctx:FlowLangParser.TransitionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#launchEventDecl.
    def visitLaunchEventDecl(self, ctx:FlowLangParser.LaunchEventDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#eventAction.
    def visitEventAction(self, ctx:FlowLangParser.EventActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#interfaceDecl.
    def visitInterfaceDecl(self, ctx:FlowLangParser.InterfaceDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#messageDecl.
    def visitMessageDecl(self, ctx:FlowLangParser.MessageDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#serviceDecl_interface.
    def visitServiceDecl_interface(self, ctx:FlowLangParser.ServiceDecl_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#requestBlock.
    def visitRequestBlock(self, ctx:FlowLangParser.RequestBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#responseBlock.
    def visitResponseBlock(self, ctx:FlowLangParser.ResponseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#actionDecl_interface.
    def visitActionDecl_interface(self, ctx:FlowLangParser.ActionDecl_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#goalBlock.
    def visitGoalBlock(self, ctx:FlowLangParser.GoalBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#feedbackBlock.
    def visitFeedbackBlock(self, ctx:FlowLangParser.FeedbackBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#resultBlock.
    def visitResultBlock(self, ctx:FlowLangParser.ResultBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#expression.
    def visitExpression(self, ctx:FlowLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:FlowLangParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#literal.
    def visitLiteral(self, ctx:FlowLangParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#expressionList.
    def visitExpressionList(self, ctx:FlowLangParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#fieldInitializer.
    def visitFieldInitializer(self, ctx:FlowLangParser.FieldInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#parameterList.
    def visitParameterList(self, ctx:FlowLangParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#parameter.
    def visitParameter(self, ctx:FlowLangParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#argumentList.
    def visitArgumentList(self, ctx:FlowLangParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#argument.
    def visitArgument(self, ctx:FlowLangParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#qualifiedIdentifier.
    def visitQualifiedIdentifier(self, ctx:FlowLangParser.QualifiedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FlowLangParser#identifier.
    def visitIdentifier(self, ctx:FlowLangParser.IdentifierContext):
        return self.visitChildren(ctx)



del FlowLangParser