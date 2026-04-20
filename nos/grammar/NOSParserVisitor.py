# Generated from nos/grammar/NOSParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .NOSParser import NOSParser
else:
    from NOSParser import NOSParser

# This class defines a complete generic visitor for a parse tree produced by NOSParser.

class NOSParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NOSParser#nosFile.
    def visitNosFile(self, ctx:NOSParser.NosFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#packageDecl.
    def visitPackageDecl(self, ctx:NOSParser.PackageDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#version.
    def visitVersion(self, ctx:NOSParser.VersionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#depends.
    def visitDepends(self, ctx:NOSParser.DependsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#importDecl.
    def visitImportDecl(self, ctx:NOSParser.ImportDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#nodeDecl.
    def visitNodeDecl(self, ctx:NOSParser.NodeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#nodeBody.
    def visitNodeBody(self, ctx:NOSParser.NodeBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#parameterBlock.
    def visitParameterBlock(self, ctx:NOSParser.ParameterBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#parameterDecl.
    def visitParameterDecl(self, ctx:NOSParser.ParameterDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#constraint.
    def visitConstraint(self, ctx:NOSParser.ConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#typeSpec.
    def visitTypeSpec(self, ctx:NOSParser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#primitiveType.
    def visitPrimitiveType(self, ctx:NOSParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#fieldDecl.
    def visitFieldDecl(self, ctx:NOSParser.FieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#subscriptionBlock.
    def visitSubscriptionBlock(self, ctx:NOSParser.SubscriptionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#subscriptionDecl.
    def visitSubscriptionDecl(self, ctx:NOSParser.SubscriptionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#publicationBlock.
    def visitPublicationBlock(self, ctx:NOSParser.PublicationBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#publicationDecl.
    def visitPublicationDecl(self, ctx:NOSParser.PublicationDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#serviceBlock.
    def visitServiceBlock(self, ctx:NOSParser.ServiceBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#serviceDecl.
    def visitServiceDecl(self, ctx:NOSParser.ServiceDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#actionBlock.
    def visitActionBlock(self, ctx:NOSParser.ActionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#actionDecl.
    def visitActionDecl(self, ctx:NOSParser.ActionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#lifecycleDecl.
    def visitLifecycleDecl(self, ctx:NOSParser.LifecycleDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#componentBlock.
    def visitComponentBlock(self, ctx:NOSParser.ComponentBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#componentDecl.
    def visitComponentDecl(self, ctx:NOSParser.ComponentDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#parameterOverride.
    def visitParameterOverride(self, ctx:NOSParser.ParameterOverrideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#callbackDecl.
    def visitCallbackDecl(self, ctx:NOSParser.CallbackDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#pythonCode.
    def visitPythonCode(self, ctx:NOSParser.PythonCodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#launchDecl.
    def visitLaunchDecl(self, ctx:NOSParser.LaunchDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#launchBody.
    def visitLaunchBody(self, ctx:NOSParser.LaunchBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#argumentBlock.
    def visitArgumentBlock(self, ctx:NOSParser.ArgumentBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#argumentDecl.
    def visitArgumentDecl(self, ctx:NOSParser.ArgumentDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#groupDecl.
    def visitGroupDecl(self, ctx:NOSParser.GroupDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#nodeInstance.
    def visitNodeInstance(self, ctx:NOSParser.NodeInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#nodeConfig.
    def visitNodeConfig(self, ctx:NOSParser.NodeConfigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#remapDecl.
    def visitRemapDecl(self, ctx:NOSParser.RemapDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#containerDecl.
    def visitContainerDecl(self, ctx:NOSParser.ContainerDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#componentInstance.
    def visitComponentInstance(self, ctx:NOSParser.ComponentInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#includeDecl.
    def visitIncludeDecl(self, ctx:NOSParser.IncludeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#includeArgs.
    def visitIncludeArgs(self, ctx:NOSParser.IncludeArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#namedArgument.
    def visitNamedArgument(self, ctx:NOSParser.NamedArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#lifecycleManagerDecl.
    def visitLifecycleManagerDecl(self, ctx:NOSParser.LifecycleManagerDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#managesBlock.
    def visitManagesBlock(self, ctx:NOSParser.ManagesBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#transitionBlock.
    def visitTransitionBlock(self, ctx:NOSParser.TransitionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#transitionDecl.
    def visitTransitionDecl(self, ctx:NOSParser.TransitionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#launchEventDecl.
    def visitLaunchEventDecl(self, ctx:NOSParser.LaunchEventDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#eventAction.
    def visitEventAction(self, ctx:NOSParser.EventActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#interfaceDecl.
    def visitInterfaceDecl(self, ctx:NOSParser.InterfaceDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#messageDecl.
    def visitMessageDecl(self, ctx:NOSParser.MessageDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#serviceDecl_interface.
    def visitServiceDecl_interface(self, ctx:NOSParser.ServiceDecl_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#requestBlock.
    def visitRequestBlock(self, ctx:NOSParser.RequestBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#responseBlock.
    def visitResponseBlock(self, ctx:NOSParser.ResponseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#actionDecl_interface.
    def visitActionDecl_interface(self, ctx:NOSParser.ActionDecl_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#goalBlock.
    def visitGoalBlock(self, ctx:NOSParser.GoalBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#feedbackBlock.
    def visitFeedbackBlock(self, ctx:NOSParser.FeedbackBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#resultBlock.
    def visitResultBlock(self, ctx:NOSParser.ResultBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#expression.
    def visitExpression(self, ctx:NOSParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:NOSParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#literal.
    def visitLiteral(self, ctx:NOSParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#expressionList.
    def visitExpressionList(self, ctx:NOSParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#fieldInitializer.
    def visitFieldInitializer(self, ctx:NOSParser.FieldInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#parameterList.
    def visitParameterList(self, ctx:NOSParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#parameter.
    def visitParameter(self, ctx:NOSParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#argumentList.
    def visitArgumentList(self, ctx:NOSParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#argument.
    def visitArgument(self, ctx:NOSParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#qualifiedIdentifier.
    def visitQualifiedIdentifier(self, ctx:NOSParser.QualifiedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NOSParser#identifier.
    def visitIdentifier(self, ctx:NOSParser.IdentifierContext):
        return self.visitChildren(ctx)



del NOSParser
