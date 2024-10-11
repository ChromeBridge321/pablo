import ply.lex as lex

# List of token names
tokens = (
    'NUMERO',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'PARENTESIS_I',
    'PARENTESIS_D',
    'ASIGNACION',
    'VARIABLE',
    'CADENA',
    'LLAVE_I',
    'LLAVE_D',
    'MAYORQ',
    'MENORQ',
    'IGUAL',
    'DIFF',
    'INCRE'
    
)

# Reserved words
reserved = {
    'si': 'SI',
    'sino': 'SINO',
    'para': 'PARA',
    'mientras': 'MIENTRAS',
    'imprimir': 'IMPRIMIR',  # Aquí está IMPRIMIR
}

# Tokens list includes reserved words
tokens = ['MULTIPLICACION', 'PARENTESIS_I', 'PARENTESIS_D', 'ASIGNACION', 
 'DIVISION', 'VARIABLE', 'LLAVE_I', 'LLAVE_D', 'NUMERO', 'CADENA', 
 'MAYORQ', 'MENORQ', 'RESTA', 'IGUAL','INCRE', 'SUMA', 'DIFF'] + list(reserved.values())

# Regular expression rules for simple tokens
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_PARENTESIS_I = r'\('
t_PARENTESIS_D = r'\)'
t_LLAVE_I = r'\{'
t_LLAVE_D = r'\}'
t_ASIGNACION = r'='
t_MAYORQ = r'>'
t_MENORQ = r'<'
t_IGUAL = r'=='
t_INCRE = r'\+\+'
t_DIFF = r'!='
t_CADENA = r'\"([^\\\n]|(\\.))*?\"'

# Rule for recognizing reserved words and variables
def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.value = t.value.lower()  # Convertimos la entrada a minúsculas
    t.type = reserved.get(t.value, 'VARIABLE')  # Check for reserved words
    return t

# Rule for recognizing numbers
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
hola ++
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
##