parser grammar NOSParser;

options {
    tokenVocab = NOSLexer;
}

// Entry point
nosFile: packageDecl? importDecl* (nodeDecl | launchDecl | interfaceDecl)* EOF;

// Package declaration
packageDecl: PACKAGE identifier version? depends?;
version: VERSION STRING_LITERAL;
depends: DEPENDS COLON LBRACKET STRING_LITERAL (COMMA STRING_LITERAL)* RBRACKET;

// Import declarations
importDecl: IMPORT qualifiedIdentifier (AS identifier)?;

// Node declaration
nodeDecl: NODE identifier LBRACE nodeBody RBRACE;

nodeBody:
    parameterBlock?
    subscriptionBlock?
    publicationBlock?
    serviceBlock?
    actionBlock?
    lifecycleDecl?
    componentBlock?
    callbackDecl*
;

// Parameter block
parameterBlock: PARAMETERS LBRACE parameterDecl* RBRACE;

parameterDecl:
    identifier COLON typeSpec (ASSIGN expression)? constraint*;

constraint: AT identifier (LPAREN argumentList? RPAREN | expression)?;

// Type definitions
typeSpec:
    primitiveType
    | qualifiedIdentifier
    | LIST LT typeSpec GT
    | STRUCT LBRACE fieldDecl* RBRACE
;

primitiveType:
    BOOL
    | INT
    | FLOAT
    | DOUBLE
    | STRING
    | DURATION
    | TIME
;

fieldDecl: identifier COLON typeSpec (ASSIGN expression)? constraint*;

// Communication blocks
subscriptionBlock: SUBSCRIPTIONS LBRACE subscriptionDecl* RBRACE;
subscriptionDecl:
    identifier COLON qualifiedIdentifier AT TOPIC LPAREN expression RPAREN constraint*;

publicationBlock: PUBLICATIONS LBRACE publicationDecl* RBRACE;
publicationDecl:
    identifier COLON qualifiedIdentifier AT TOPIC LPAREN expression RPAREN constraint*;

serviceBlock: SERVICES LBRACE serviceDecl* RBRACE;
serviceDecl:
    identifier COLON qualifiedIdentifier AT SERVICE LPAREN expression RPAREN constraint*;

actionBlock: ACTIONS LBRACE actionDecl* RBRACE;
actionDecl:
    identifier COLON qualifiedIdentifier constraint*;

// Lifecycle declaration
lifecycleDecl: LIFECYCLE COLON (MANAGED | UNMANAGED);

// Component block
componentBlock: COMPONENTS LBRACE componentDecl* RBRACE;
componentDecl:
    identifier COLON identifier LBRACE parameterOverride* RBRACE;

parameterOverride: identifier COLON expression;

// Callback declarations
callbackDecl:
    ON_INIT PYTHON_START pythonCode RBRACE
    | ON_SHUTDOWN PYTHON_START pythonCode RBRACE
    | ON_PARAMETER_CHANGE LPAREN parameterList? RPAREN PYTHON_START pythonCode RBRACE
    | ON identifier LPAREN parameterList? RPAREN PYTHON_START pythonCode RBRACE
;

pythonCode: (PYTHON_CODE | LBRACE pythonCode RBRACE)*;

// Launch declaration
launchDecl: LAUNCH identifier LBRACE launchBody RBRACE;

launchBody:
    argumentBlock?
    groupDecl*
    containerDecl*
    includeDecl*
    lifecycleManagerDecl?
    launchEventDecl*
;

argumentBlock: ARGUMENTS LBRACE argumentDecl* RBRACE;
argumentDecl:
    identifier COLON typeSpec (ASSIGN expression)? constraint*;

groupDecl: GROUP identifier AT NAMESPACE LPAREN expression RPAREN LBRACE nodeInstance* RBRACE;

nodeInstance:
    identifier COLON identifier LBRACE nodeConfig* RBRACE constraint*;

nodeConfig:
    PARAMETERS COLON LBRACE parameterOverride* RBRACE
    | REMAP COLON LBRACE remapDecl* RBRACE
;

remapDecl: identifier ARROW STRING_LITERAL;

containerDecl:
    CONTAINER identifier AT CONTAINER LPAREN expression RPAREN LBRACE componentInstance* RBRACE
;

componentInstance:
    identifier COLON identifier AT LOAD_COMPONENT constraint*;

includeDecl:
    INCLUDE identifier LBRACE includeArgs? RBRACE
    | INCLUDE STRING_LITERAL LBRACE includeArgs? RBRACE
;

includeArgs: ARGS COLON LBRACE namedArgument* RBRACE;
namedArgument: identifier COLON expression;

lifecycleManagerDecl:
    LIFECYCLE identifier identifier LBRACE managesBlock transitionBlock? RBRACE
;

managesBlock: MANAGES COLON LBRACKET identifier (COMMA identifier)* RBRACKET;
transitionBlock: TRANSITIONS COLON LBRACE transitionDecl* RBRACE;
transitionDecl:
    LBRACE FROM COLON identifier COMMA TO COLON identifier constraint* RBRACE
;

launchEventDecl: ON STRING_LITERAL LBRACE eventAction* RBRACE;
eventAction: identifier DOT identifier ASSIGN expression;

// Interface declaration
interfaceDecl: messageDecl | serviceDecl_interface | actionDecl_interface;

messageDecl:
    MESSAGE identifier AT ID LPAREN INT_LITERAL RPAREN LBRACE fieldDecl* RBRACE
;

serviceDecl_interface:
    SERVICE identifier AT ID LPAREN INT_LITERAL RPAREN LBRACE requestBlock responseBlock RBRACE
;

requestBlock: REQUEST LBRACE fieldDecl* RBRACE;
responseBlock: RESPONSE LBRACE fieldDecl* RBRACE;

actionDecl_interface:
    ACTION identifier AT ID LPAREN INT_LITERAL RPAREN LBRACE goalBlock feedbackBlock resultBlock RBRACE
;

goalBlock: GOAL LBRACE fieldDecl* RBRACE;
feedbackBlock: FEEDBACK LBRACE fieldDecl* RBRACE;
resultBlock: RESULT LBRACE fieldDecl* RBRACE;

// Expressions
expression:
    primaryExpression                         # PrimaryExpr
    | expression DOT identifier               # MemberAccessExpr
    | expression LBRACKET expression RBRACKET # IndexExpr
    | expression LPAREN argumentList? RPAREN  # CallExpr
    | DOLLAR LBRACE expression RBRACE         # InterpolatedExpr
    | NOT expression                          # UnaryExpr
    | expression (STAR | SLASH | MOD) expression # MultiplicativeExpr
    | expression (PLUS | MINUS) expression    # AdditiveExpr
    | expression (EQ | NEQ | LT | GT | LE | GE) expression # RelationalExpr
    | expression AND expression               # LogicalAndExpr
    | expression OR expression                # LogicalOrExpr
;

primaryExpression:
    identifier
    | literal
    | LPAREN expression RPAREN
;

literal:
    INT_LITERAL
    | FLOAT_LITERAL
    | STRING_LITERAL
    | DURATION_LITERAL
    | TRUE
    | FALSE
    | LBRACKET expressionList? RBRACKET
    | STRUCT LBRACE fieldInitializer* RBRACE
;

expressionList: expression (COMMA expression)*;
fieldInitializer: identifier COLON expression;

parameterList: parameter (COMMA parameter)*;
parameter: identifier COLON typeSpec;

argumentList: argument (COMMA argument)*;
argument: (identifier ASSIGN)? expression;

// Qualified identifiers
qualifiedIdentifier: identifier (SCOPE identifier)*;
identifier: IDENTIFIER;
