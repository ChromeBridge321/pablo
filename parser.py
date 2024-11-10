import ply.yacc as yacc
from grammar import tokens  

precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('right', 'UMINUS'),
)

variables = {}

def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement PUNTOCOMA
                     | statement_list statement PUNTOCOMA'''
    if len(p) == 3:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_statement_assign(p):
    'statement : VARIABLE ASIGNACION expression'
    variables[p[1]] = p[3]
    p[0] = ('assign', p[1], p[3])

def p_statement_expr(p):
    'statement : expression'
    p[0] = ('expr', p[1])

def p_statement_increment(p):
    'statement : VARIABLE INCRE'
    p[0] = ('increment', p[1])

# Nueva regla para SI
def p_statement_if(p):
    'statement : SI PARENTESIS_I condicion PARENTESIS_D LLAVE_I statement_list LLAVE_D'
    p[0] = ('si', p[3], p[6])

# Nueva regla para SI-SINO
def p_statement_if_else(p):
    'statement : SI PARENTESIS_I condicion PARENTESIS_D LLAVE_I statement_list LLAVE_D SINO LLAVE_I statement_list LLAVE_D'
    p[0] = ('si_sino', p[3], p[6], p[10])

# Nueva regla para PARA
def p_statement_for(p):
    'statement : PARA PARENTESIS_I statement_list condicion PUNTOCOMA statement PARENTESIS_D LLAVE_I statement_list LLAVE_D'
    p[0] = ('para', p[3], p[4], p[6], p[9])

def p_expression_binop(p):
    '''expression : expression SUMA expression
                  | expression RESTA expression
                  | expression MULTIPLICACION expression
                  | expression DIVISION expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_uminus(p):
    'expression : RESTA expression %prec UMINUS'
    p[0] = ('uminus', p[2])

def p_expression_group(p):
    'expression : PARENTESIS_I expression PARENTESIS_D'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMERO'
    p[0] = ('number', p[1])

def p_expression_string(p):
    'expression : CADENA'
    p[0] = ('string', p[1][1:-1])

def p_expression_variable(p):
    'expression : VARIABLE'
    p[0] = ('var', p[1])

def p_print_statement(p):
    'statement : IMPRIMIR PARENTESIS_I expression PARENTESIS_D'
    p[0] = ('print', p[3])

def p_condicion(p):
    '''condicion : expression MAYORQ expression
                 | expression MENORQ expression
                 | expression IGUAL expression
                 | expression DIFF expression'''
    p[0] = (p[2], p[1], p[3])

def p_mientras(p):
    'statement : MIENTRAS PARENTESIS_I condicion PARENTESIS_D LLAVE_I statement_list LLAVE_D'
    p[0] = ('mientras', p[3], p[6])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

def eval_expr(expr):
    if isinstance(expr, tuple):
        if expr[0] == 'number':
            return expr[1]
        elif expr[0] == 'string':
            return expr[1]
        elif expr[0] == 'var':
            return variables.get(expr[1], 0)
        elif expr[0] == 'uminus':
            return -eval_expr(expr[1])
        elif expr[0] in ['+', '-', '*', '/']:
            left = eval_expr(expr[1])
            right = eval_expr(expr[2])
            if expr[0] == '+': return left + right
            elif expr[0] == '-': return left - right
            elif expr[0] == '*': return left * right
            elif expr[0] == '/': return left / right
    return expr

def eval_condition(cond):
    op, left, right = cond
    left_val = eval_expr(left)
    right_val = eval_expr(right)
    if op == '>': return left_val > right_val
    elif op == '<': return left_val < right_val
    elif op == '==': return left_val == right_val
    elif op == '!=': return left_val != right_val

def interpret(program):
    result = None
    if not program:
        return result
        
    for statement in program:
        if statement[0] == 'assign':
            variables[statement[1]] = eval_expr(statement[2])
        elif statement[0] == 'expr':
            result = eval_expr(statement[1])
        elif statement[0] == 'print':
            print(eval_expr(statement[1]))
        elif statement[0] == 'increment':
            variables[statement[1]] = variables.get(statement[1], 0) + 1
        elif statement[0] == 'mientras':
            condition, body = statement[1], statement[2]
            while eval_condition(condition):
                interpret(body)
        elif statement[0] == 'si':
            condition, body = statement[1], statement[2]
            if eval_condition(condition):
                interpret(body)
        elif statement[0] == 'si_sino':
            condition, if_body, else_body = statement[1], statement[2], statement[3]
            if eval_condition(condition):
                interpret(if_body)
            else:
                interpret(else_body)
        elif statement[0] == 'para':
            init, condition, step, body = statement[1], statement[2], statement[3], statement[4]
            interpret(init)
            while eval_condition(condition):
                interpret(body)
                interpret([step])
    return result

# REPL
def parse_and_interpret(code):
    try:
        result = parser.parse(code)  # Pasa el contenido al parser
        if result is not None:
            return interpret(result)  # Interpreta el resultado
    except Exception as e:
        return f"Ocurrió un error: {e}"
