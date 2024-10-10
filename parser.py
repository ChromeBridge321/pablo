import ply.yacc as yacc
from grammar import tokens  # Asegúrate de cargar correctamente los tokens del lexer



precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('right', 'UMINUS'),
)

# Dictionary to store variables
variables = {}

def p_statement_assign(p):
    'statement : VARIABLE ASIGNACION expression'
    variables[p[1]] = p[3]
    p[0] = p[3]

def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression SUMA expression
                  | expression RESTA expression
                  | expression MULTIPLICACION expression
                  | expression DIVISION expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expression_uminus(p):
    'expression : RESTA expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_group(p):
    'expression : PARENTESIS_I expression PARENTESIS_D'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMERO'
    p[0] = p[1]

def p_expression_string(p):
    'expression : CADENA'
    p[0] = p[1][1:-1]  # Remove the quotation marks

def p_expression_variable(p):
    'expression : VARIABLE'
    try:
        p[0] = variables[p[1]]
    except LookupError:
        print(f"Undefined variable '{p[1]}'")
        p[0] = 0

def p_print_statement(p):
    'statement : IMPRIMIR PARENTESIS_I expression PARENTESIS_D'
    print(p[3])
    p[0] = None

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# REPL
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    if result is not None:
        print(result)
        #####