import ply.yacc as yacc
# Get the token map from the lexer.  This is required.
from grammar import tokens


precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('left', 'PARENTESIS_I', 'PARENTESIS_D'),
)
def p_expression_plus(p):
    'expression : expression SUMA term'
    p[0] = p[1] + p[3]

def p_expressions(p):
    '''expression : expression RESTA expression
                  | RESTA expression'''
    if (len(p) == 4):
        p[0] = p[1] - p[3]
    elif (len(p) == 3):
        p[0] = -p[2]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term MULTIPLICACION factor'
    p[0] = p[1] * p[3]


def p_term_div(p):
    'term : term DIVISION factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMERO'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : PARENTESIS_I expression PARENTESIS_D'
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)