# Generated from nos/grammar/NOSParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .NOSParser import NOSParser
else:
    from NOSParser import NOSParser

# This class defines a complete listener for a parse tree produced by NOSParser.
class NOSParserListener(ParseTreeListener):

    # Enter a parse tree produced by NOSParser#nosFile.
    def enterNosFile(self, ctx:NOSParser.NosFileContext):
        pass

    # Exit a parse tree produced by NOSParser#nosFile.
    def exitNosFile(self, ctx:NOSParser.NosFileContext):
        pass


    # Enter a parse tree produced by NOSParser#packageDecl.
    def enterPackageDecl(self, ctx:NOSParser.PackageDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#packageDecl.
    def exitPackageDecl(self, ctx:NOSParser.PackageDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#version.
    def enterVersion(self, ctx:NOSParser.VersionContext):
        pass

    # Exit a parse tree produced by NOSParser#version.
    def exitVersion(self, ctx:NOSParser.VersionContext):
        pass


    # Enter a parse tree produced by NOSParser#depends.
    def enterDepends(self, ctx:NOSParser.DependsContext):
        pass

    # Exit a parse tree produced by NOSParser#depends.
    def exitDepends(self, ctx:NOSParser.DependsContext):
        pass


    # Enter a parse tree produced by NOSParser#importDecl.
    def enterImportDecl(self, ctx:NOSParser.ImportDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#importDecl.
    def exitImportDecl(self, ctx:NOSParser.ImportDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#nodeDecl.
    def enterNodeDecl(self, ctx:NOSParser.NodeDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#nodeDecl.
    def exitNodeDecl(self, ctx:NOSParser.NodeDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#nodeBody.
    def enterNodeBody(self, ctx:NOSParser.NodeBodyContext):
        pass

    # Exit a parse tree produced by NOSParser#nodeBody.
    def exitNodeBody(self, ctx:NOSParser.NodeBodyContext):
        pass


    # Enter a parse tree produced by NOSParser#parameterBlock.
    def enterParameterBlock(self, ctx:NOSParser.ParameterBlockContext):
        pass

    # Exit a parse tree produced by NOSParser#parameterBlock.
    def exitParameterBlock(self, ctx:NOSParser.ParameterBlockContext):
        pass


    # Enter a parse tree produced by NOSParser#parameterDecl.
    def enterParameterDecl(self, ctx:NOSParser.ParameterDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#parameterDecl.
    def exitParameterDecl(self, ctx:NOSParser.ParameterDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#constraint.
    def enterConstraint(self, ctx:NOSParser.ConstraintContext):
        pass

    # Exit a parse tree produced by NOSParser#constraint.
    def exitConstraint(self, ctx:NOSParser.ConstraintContext):
        pass


    # Enter a parse tree produced by NOSParser#typeSpec.
    def enterTypeSpec(self, ctx:NOSParser.TypeSpecContext):
        pass

    # Exit a parse tree produced by NOSParser#typeSpec.
    def exitTypeSpec(self, ctx:NOSParser.TypeSpecContext):
        pass


    # Enter a parse tree produced by NOSParser#primitiveType.
    def enterPrimitiveType(self, ctx:NOSParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by NOSParser#primitiveType.
    def exitPrimitiveType(self, ctx:NOSParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by NOSParser#fieldDecl.
    def enterFieldDecl(self, ctx:NOSParser.FieldDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#fieldDecl.
    def exitFieldDecl(self, ctx:NOSParser.FieldDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#subscriptionBlock.
    def enterSubscriptionBlock(self, ctx:NOSParser.SubscriptionBlockContext):
        pass

    # Exit a parse tree produced by NOSParser#subscriptionBlock.
    def exitSubscriptionBlock(self, ctx:NOSParser.SubscriptionBlockContext):
        pass


    # Enter a parse tree produced by NOSParser#subscriptionDecl.
    def enterSubscriptionDecl(self, ctx:NOSParser.SubscriptionDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#subscriptionDecl.
    def exitSubscriptionDecl(self, ctx:NOSParser.SubscriptionDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#publicationBlock.
    def enterPublicationBlock(self, ctx:NOSParser.PublicationBlockContext):
        pass

    # Exit a parse tree produced by NOSParser#publicationBlock.
    def exitPublicationBlock(self, ctx:NOSParser.PublicationBlockContext):
        pass


    # Enter a parse tree produced by NOSParser#publicationDecl.
    def enterPublicationDecl(self, ctx:NOSParser.PublicationDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#publicationDecl.
    def exitPublicationDecl(self, ctx:NOSParser.PublicationDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#serviceBlock.
    def enterServiceBlock(self, ctx:NOSParser.ServiceBlockContext):
        pass

    # Exit a parse tree produced by NOSParser#serviceBlock.
    def exitServiceBlock(self, ctx:NOSParser.ServiceBlockContext):
        pass


    # Enter a parse tree produced by NOSParser#serviceDecl.
    def enterServiceDecl(self, ctx:NOSParser.ServiceDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#serviceDecl.
    def exitServiceDecl(self, ctx:NOSParser.ServiceDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#actionBlock.
    def enterActionBlock(self, ctx:NOSParser.ActionBlockContext):
        pass

    # Exit a parse tree produced by NOSParser#actionBlock.
    def exitActionBlock(self, ctx:NOSParser.ActionBlockContext):
        pass


    # Enter a parse tree produced by NOSParser#actionDecl.
    def enterActionDecl(self, ctx:NOSParser.ActionDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#actionDecl.
    def exitActionDecl(self, ctx:NOSParser.ActionDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#lifecycleDecl.
    def enterLifecycleDecl(self, ctx:NOSParser.LifecycleDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#lifecycleDecl.
    def exitLifecycleDecl(self, ctx:NOSParser.LifecycleDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#componentBlock.
    def enterComponentBlock(self, ctx:NOSParser.ComponentBlockContext):
        pass

    # Exit a parse tree produced by NOSParser#componentBlock.
    def exitComponentBlock(self, ctx:NOSParser.ComponentBlockContext):
        pass


    # Enter a parse tree produced by NOSParser#componentDecl.
    def enterComponentDecl(self, ctx:NOSParser.ComponentDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#componentDecl.
    def exitComponentDecl(self, ctx:NOSParser.ComponentDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#parameterOverride.
    def enterParameterOverride(self, ctx:NOSParser.ParameterOverrideContext):
        pass

    # Exit a parse tree produced by NOSParser#parameterOverride.
    def exitParameterOverride(self, ctx:NOSParser.ParameterOverrideContext):
        pass


    # Enter a parse tree produced by NOSParser#callbackDecl.
    def enterCallbackDecl(self, ctx:NOSParser.CallbackDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#callbackDecl.
    def exitCallbackDecl(self, ctx:NOSParser.CallbackDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#pythonCode.
    def enterPythonCode(self, ctx:NOSParser.PythonCodeContext):
        pass

    # Exit a parse tree produced by NOSParser#pythonCode.
    def exitPythonCode(self, ctx:NOSParser.PythonCodeContext):
        pass


    # Enter a parse tree produced by NOSParser#launchDecl.
    def enterLaunchDecl(self, ctx:NOSParser.LaunchDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#launchDecl.
    def exitLaunchDecl(self, ctx:NOSParser.LaunchDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#launchBody.
    def enterLaunchBody(self, ctx:NOSParser.LaunchBodyContext):
        pass

    # Exit a parse tree produced by NOSParser#launchBody.
    def exitLaunchBody(self, ctx:NOSParser.LaunchBodyContext):
        pass


    # Enter a parse tree produced by NOSParser#argumentBlock.
    def enterArgumentBlock(self, ctx:NOSParser.ArgumentBlockContext):
        pass

    # Exit a parse tree produced by NOSParser#argumentBlock.
    def exitArgumentBlock(self, ctx:NOSParser.ArgumentBlockContext):
        pass


    # Enter a parse tree produced by NOSParser#argumentDecl.
    def enterArgumentDecl(self, ctx:NOSParser.ArgumentDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#argumentDecl.
    def exitArgumentDecl(self, ctx:NOSParser.ArgumentDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#groupDecl.
    def enterGroupDecl(self, ctx:NOSParser.GroupDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#groupDecl.
    def exitGroupDecl(self, ctx:NOSParser.GroupDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#nodeInstance.
    def enterNodeInstance(self, ctx:NOSParser.NodeInstanceContext):
        pass

    # Exit a parse tree produced by NOSParser#nodeInstance.
    def exitNodeInstance(self, ctx:NOSParser.NodeInstanceContext):
        pass


    # Enter a parse tree produced by NOSParser#nodeConfig.
    def enterNodeConfig(self, ctx:NOSParser.NodeConfigContext):
        pass

    # Exit a parse tree produced by NOSParser#nodeConfig.
    def exitNodeConfig(self, ctx:NOSParser.NodeConfigContext):
        pass


    # Enter a parse tree produced by NOSParser#remapDecl.
    def enterRemapDecl(self, ctx:NOSParser.RemapDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#remapDecl.
    def exitRemapDecl(self, ctx:NOSParser.RemapDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#containerDecl.
    def enterContainerDecl(self, ctx:NOSParser.ContainerDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#containerDecl.
    def exitContainerDecl(self, ctx:NOSParser.ContainerDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#componentInstance.
    def enterComponentInstance(self, ctx:NOSParser.ComponentInstanceContext):
        pass

    # Exit a parse tree produced by NOSParser#componentInstance.
    def exitComponentInstance(self, ctx:NOSParser.ComponentInstanceContext):
        pass


    # Enter a parse tree produced by NOSParser#includeDecl.
    def enterIncludeDecl(self, ctx:NOSParser.IncludeDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#includeDecl.
    def exitIncludeDecl(self, ctx:NOSParser.IncludeDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#includeArgs.
    def enterIncludeArgs(self, ctx:NOSParser.IncludeArgsContext):
        pass

    # Exit a parse tree produced by NOSParser#includeArgs.
    def exitIncludeArgs(self, ctx:NOSParser.IncludeArgsContext):
        pass


    # Enter a parse tree produced by NOSParser#namedArgument.
    def enterNamedArgument(self, ctx:NOSParser.NamedArgumentContext):
        pass

    # Exit a parse tree produced by NOSParser#namedArgument.
    def exitNamedArgument(self, ctx:NOSParser.NamedArgumentContext):
        pass


    # Enter a parse tree produced by NOSParser#lifecycleManagerDecl.
    def enterLifecycleManagerDecl(self, ctx:NOSParser.LifecycleManagerDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#lifecycleManagerDecl.
    def exitLifecycleManagerDecl(self, ctx:NOSParser.LifecycleManagerDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#managesBlock.
    def enterManagesBlock(self, ctx:NOSParser.ManagesBlockContext):
        pass

    # Exit a parse tree produced by NOSParser#managesBlock.
    def exitManagesBlock(self, ctx:NOSParser.ManagesBlockContext):
        pass


    # Enter a parse tree produced by NOSParser#transitionBlock.
    def enterTransitionBlock(self, ctx:NOSParser.TransitionBlockContext):
        pass

    # Exit a parse tree produced by NOSParser#transitionBlock.
    def exitTransitionBlock(self, ctx:NOSParser.TransitionBlockContext):
        pass


    # Enter a parse tree produced by NOSParser#transitionDecl.
    def enterTransitionDecl(self, ctx:NOSParser.TransitionDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#transitionDecl.
    def exitTransitionDecl(self, ctx:NOSParser.TransitionDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#launchEventDecl.
    def enterLaunchEventDecl(self, ctx:NOSParser.LaunchEventDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#launchEventDecl.
    def exitLaunchEventDecl(self, ctx:NOSParser.LaunchEventDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#eventAction.
    def enterEventAction(self, ctx:NOSParser.EventActionContext):
        pass

    # Exit a parse tree produced by NOSParser#eventAction.
    def exitEventAction(self, ctx:NOSParser.EventActionContext):
        pass


    # Enter a parse tree produced by NOSParser#interfaceDecl.
    def enterInterfaceDecl(self, ctx:NOSParser.InterfaceDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#interfaceDecl.
    def exitInterfaceDecl(self, ctx:NOSParser.InterfaceDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#messageDecl.
    def enterMessageDecl(self, ctx:NOSParser.MessageDeclContext):
        pass

    # Exit a parse tree produced by NOSParser#messageDecl.
    def exitMessageDecl(self, ctx:NOSParser.MessageDeclContext):
        pass


    # Enter a parse tree produced by NOSParser#serviceDecl_interface.
    def enterServiceDecl_interface(self, ctx:NOSParser.ServiceDecl_interfaceContext):
        pass

    # Exit a parse tree produced by NOSParser#serviceDecl_interface.
    def exitServiceDecl_interface(self, ctx:NOSParser.ServiceDecl_interfaceContext):
        pass


    # Enter a parse tree produced by NOSParser#requestBlock.
    def enterRequestBlock(self, ctx:NOSParser.RequestBlockContext):
        pass

    # Exit a parse tree produced by NOSParser#requestBlock.
    def exitRequestBlock(self, ctx:NOSParser.RequestBlockContext):
        pass


    # Enter a parse tree produced by NOSParser#responseBlock.
    def enterResponseBlock(self, ctx:NOSParser.ResponseBlockContext):
        pass

    # Exit a parse tree produced by NOSParser#responseBlock.
    def exitResponseBlock(self, ctx:NOSParser.ResponseBlockContext):
        pass


    # Enter a parse tree produced by NOSParser#actionDecl_interface.
    def enterActionDecl_interface(self, ctx:NOSParser.ActionDecl_interfaceContext):
        pass

    # Exit a parse tree produced by NOSParser#actionDecl_interface.
    def exitActionDecl_interface(self, ctx:NOSParser.ActionDecl_interfaceContext):
        pass


    # Enter a parse tree produced by NOSParser#goalBlock.
    def enterGoalBlock(self, ctx:NOSParser.GoalBlockContext):
        pass

    # Exit a parse tree produced by NOSParser#goalBlock.
    def exitGoalBlock(self, ctx:NOSParser.GoalBlockContext):
        pass


    # Enter a parse tree produced by NOSParser#feedbackBlock.
    def enterFeedbackBlock(self, ctx:NOSParser.FeedbackBlockContext):
        pass

    # Exit a parse tree produced by NOSParser#feedbackBlock.
    def exitFeedbackBlock(self, ctx:NOSParser.FeedbackBlockContext):
        pass


    # Enter a parse tree produced by NOSParser#resultBlock.
    def enterResultBlock(self, ctx:NOSParser.ResultBlockContext):
        pass

    # Exit a parse tree produced by NOSParser#resultBlock.
    def exitResultBlock(self, ctx:NOSParser.ResultBlockContext):
        pass


    # Enter a parse tree produced by NOSParser#expression.
    def enterExpression(self, ctx:NOSParser.ExpressionContext):
        pass

    # Exit a parse tree produced by NOSParser#expression.
    def exitExpression(self, ctx:NOSParser.ExpressionContext):
        pass


    # Enter a parse tree produced by NOSParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:NOSParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by NOSParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:NOSParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by NOSParser#literal.
    def enterLiteral(self, ctx:NOSParser.LiteralContext):
        pass

    # Exit a parse tree produced by NOSParser#literal.
    def exitLiteral(self, ctx:NOSParser.LiteralContext):
        pass


    # Enter a parse tree produced by NOSParser#expressionList.
    def enterExpressionList(self, ctx:NOSParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by NOSParser#expressionList.
    def exitExpressionList(self, ctx:NOSParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by NOSParser#fieldInitializer.
    def enterFieldInitializer(self, ctx:NOSParser.FieldInitializerContext):
        pass

    # Exit a parse tree produced by NOSParser#fieldInitializer.
    def exitFieldInitializer(self, ctx:NOSParser.FieldInitializerContext):
        pass


    # Enter a parse tree produced by NOSParser#parameterList.
    def enterParameterList(self, ctx:NOSParser.ParameterListContext):
        pass

    # Exit a parse tree produced by NOSParser#parameterList.
    def exitParameterList(self, ctx:NOSParser.ParameterListContext):
        pass


    # Enter a parse tree produced by NOSParser#parameter.
    def enterParameter(self, ctx:NOSParser.ParameterContext):
        pass

    # Exit a parse tree produced by NOSParser#parameter.
    def exitParameter(self, ctx:NOSParser.ParameterContext):
        pass


    # Enter a parse tree produced by NOSParser#argumentList.
    def enterArgumentList(self, ctx:NOSParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by NOSParser#argumentList.
    def exitArgumentList(self, ctx:NOSParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by NOSParser#argument.
    def enterArgument(self, ctx:NOSParser.ArgumentContext):
        pass

    # Exit a parse tree produced by NOSParser#argument.
    def exitArgument(self, ctx:NOSParser.ArgumentContext):
        pass


    # Enter a parse tree produced by NOSParser#qualifiedIdentifier.
    def enterQualifiedIdentifier(self, ctx:NOSParser.QualifiedIdentifierContext):
        pass

    # Exit a parse tree produced by NOSParser#qualifiedIdentifier.
    def exitQualifiedIdentifier(self, ctx:NOSParser.QualifiedIdentifierContext):
        pass


    # Enter a parse tree produced by NOSParser#identifier.
    def enterIdentifier(self, ctx:NOSParser.IdentifierContext):
        pass

    # Exit a parse tree produced by NOSParser#identifier.
    def exitIdentifier(self, ctx:NOSParser.IdentifierContext):
        pass



del NOSParser
