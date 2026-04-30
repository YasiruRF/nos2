lexer grammar NOSLexer;

channels {
    PYTHON_CHANNEL
}

// Keywords
PACKAGE     : 'package';
VERSION     : 'version';
DEPENDS     : 'depends';
IMPORT      : 'import';
AS          : 'as';
NODE        : 'node';
PARAMETERS  : 'parameters';
SUBSCRIPTIONS: 'subscriptions';
PUBLICATIONS: 'publications';
SERVICES    : 'services';
ACTIONS     : 'actions';
ACTION      : 'action';
LIFECYCLE   : 'lifecycle';
COMPONENTS  : 'components';
ON          : 'on';
ON_INIT     : 'on_init';
ON_SHUTDOWN : 'on_shutdown';
ON_PARAMETER_CHANGE: 'on_parameter_change';
LAUNCH      : 'launch';
GROUP       : 'group';
CONTAINER   : 'container';
INCLUDE     : 'include';
ARGUMENTS   : 'arguments';
ARGS        : 'args';
NAMESPACE   : 'namespace';
TOPIC       : 'topic';
SERVICE     : 'service';
RESPONSE    : 'response';
REMAP        : 'remap';
MANAGES     : 'manages';
TRANSITIONS : 'transitions';
FROM        : 'from';
TO          : 'to';
MESSAGE     : 'message';
REQUEST     : 'request';
GOAL        : 'goal';
FEEDBACK    : 'feedback';
RESULT      : 'result';
ID          : 'id';
LOAD_COMPONENT: 'load_component';

// Types
BOOL        : 'bool';
INT         : 'int';
FLOAT       : 'float';
DOUBLE      : 'double';
STRING      : 'string';
DURATION    : 'duration';
TIME        : 'time';
LIST        : 'list';
STRUCT      : 'struct';

// Lifecycle states
MANAGED     : 'managed';
UNMANAGED   : 'unmanaged';

// Literals
TRUE        : 'true';
FALSE       : 'false';

// Operators
PLUS        : '+';
MINUS       : '-';
STAR        : '*';
SLASH       : '/';
MOD         : '%';

// Boolean operators
AND         : '&&';
OR          : '||';
NOT         : '!';

// Comparison
EQ          : '==';
NEQ         : '!=';
LE          : '<=';
GE          : '>=';
LT          : '<';
GT          : '>';

// Assignment
ASSIGN      : '=';

// Delimiters
LPAREN      : '(';
RPAREN      : ')';
LBRACE      : '{';
RBRACE      : '}';
LBRACKET    : '[';
RBRACKET    : ']';
COLON       : ':';
SEMICOLON   : ';';
COMMA       : ',';
DOT         : '.';
SCOPE       : '::';
AT          : '@';
DOLLAR      : '$';
ARROW       : '->';
PYTHON_START: '->' [ \t\r\n]* '{' -> pushMode(PYTHON_MODE);

// Literals
INT_LITERAL : [0-9]+;
FLOAT_LITERAL: [0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)?;
STRING_LITERAL: '"' (~["\r\n] | '\\' .)* '"';

// Duration literal (e.g., 30.0s, 100ms)
DURATION_LITERAL: [0-9]+ ('.' [0-9]+)? ('s' | 'ms' | 'us' | 'ns');

// Identifier
IDENTIFIER  : [a-zA-Z_][a-zA-Z0-9_]*;

// Comments and whitespace
LINE_COMMENT: ('//' | '#') ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
WS          : [ \t\r\n]+ -> skip;

// Mode for capturing Python code blocks
mode PYTHON_MODE;

PYTHON_LBRACE: '{' -> type(LBRACE), pushMode(PYTHON_MODE);
PYTHON_RBRACE: '}' -> type(RBRACE), popMode;
PYTHON_CODE:   ~[{}] +;
