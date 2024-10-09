import ply.lex as lex

# List of token names.   This is always required
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

)

reserved = {
   'si' : 'SI',
   'var' : 'VAR',
   'sino' : 'SINO',
   'para' : 'PARA',
   'mientras' : 'MIENTRAS',
   'imprimir' : 'IMPRIMIR',
}

tokens = ['MULTIPLICACION', 'PARENTESIS_I', 'PARENTESIS_D','ASIGNACION', 'DIVISION', 'VARIABLE', 'NUMERO', 'RESTA', 'SUMA'] + list(reserved.values())

# Regular expression rules for simple tokens
t_SUMA    = r'\+'
t_RESTA   = r'-'
t_MULTIPLICACION   = r'\*'
t_DIVISION  = r'/'
t_PARENTESIS_I  = r'\('
t_PARENTESIS_D  = r'\)'
t_ASIGNACION  = r'='
t_SI = r'SI'
t_SINO = r'SINO'
t_PARA = r'PARA'
t_MIENTRAS = r'MIENTRAS'
t_IMPRIMIR = r'IMPRIMIR'
t_VAR = r'VAR'
t_VARIABLE = r'[a-zA-Z_][a-zA-Z_0-9]*'

# A regular expression rule with some action code
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


# Test it out
data = '''

VAR x = 5


'''
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)