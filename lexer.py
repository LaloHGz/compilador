import ply.lex as lex

# List of reserved words
reserved = {
    'program' : 'PROGRAM',
    'main' : 'MAIN',
    'end' : 'END',
    'void' : 'VOID',
    'var' : 'VAR',
    'int' : 'INT',
    'float' : 'FLOAT',
    'print' : 'PRINT',
    'while' : 'WHILE',
    'do' : 'DO',
    'if' : 'IF',
    'else' : 'ELSE',
}

# List of toke names
tokens = [
    'ID',
    'SEMICOLON',
    'LCBRACKET',
    'RCBRACKET',
    'EQUALS',
    'CTE_INT',
    'CTE_FLOAT',
    'CTE_STRING',
    'LPARENTHESES',
    'RPARENTHESES',
    'COMMA',
    'COLON',
    'LBRACKET',
    'RBRACKET',
    'LESS',
    'GREATER',
    'NOT_EQUALS',
    'PLUS',
    'MINUS',
    'MULTIPLICATION',
    'DIVISION'
] + list(reserved.values())

# ignore empty espaces and tabs
t_ignore = ' \t\r\n'

# Regular expression rules for simple tokens
t_SEMICOLON = r';'
t_LCBRACKET = r'\{'
t_RCBRACKET = r'\}'
t_EQUALS = r'='
t_LESS = r'<'
t_GREATER = r'>'
t_NOT_EQUALS = r'!='
t_LPARENTHESES = r'\('
t_RPARENTHESES = r'\)'
t_COMMA = r','
t_COLON = r':'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'/'



# Regular expression rules for constants
def t_CTE_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CTE_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CTE_STRING(t):
    r'\".*?\"'
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, "ID")  # Verify if it's a reserved word
    return t


def t_error(t):
    print(f"Illegal character:  '{t.value[0]}'")
    t.lexer.skip(1)
    
# Build the lexer
lexer = lex.lex()