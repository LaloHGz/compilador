import ply.yacc as yacc
from lexer import tokens
from sem import D_Functions, SEM

# Create the Functions Directory
d_functions = D_Functions()

# Create list of temporary ids
temp_ids = []


# Parsing rules
def p_Programa(p):
    'Programa : PROGRAM ID ACTION_1 SEMICOLON Declare_var Declare_func MAIN BODY END'
    
# Initialize D_Functions & D_Vars 
def p_action_1(p):
    'ACTION_1 :'
    # 1.- Add the first function program name
    d_functions.add_function(p[-1],"NP")
    d_functions.set_global_function(p[-1])


def p_Declare_var(p):
    '''Declare_var : VARS
                   | vacio'''

def p_VARS(p):
    'VARS : VAR Variables'

def p_Variables(p):
    'Variables : List_ids COLON Type SEMICOLON More_variables'

def p_More_variables(p):
    '''More_variables : Variables
                      | vacio'''

def p_List_ids(p):
    'List_ids : ID ACTION_2 More_ids'

def p_action_2(p):
    'ACTION_2 :'
    # 2.- Temporarily save the list of ids
    temp_ids.append(p[-1])

def p_More_ids(p):
    '''More_ids : COMMA List_ids
                | vacio'''

def p_Type(p):
    '''Type : INT ACTION_3
            | FLOAT ACTION_3'''

def p_action_3(p):
    'ACTION_3 :'
    # 3.- Add all the variables of the current function & clear temp_ids
    for temp_id in temp_ids:
        d_functions.add_variable(temp_id,p[-1])
    temp_ids.clear()

def p_Declare_func(p):
    '''Declare_func : FUNCS More_func
                    | vacio'''

def p_More_func(p):
    '''More_func : Declare_func
                 | vacio'''

def p_FUNCS(p):
    'FUNCS : VOID ID ACTION_4 LPARENTHESES Parameters RPARENTHESES LBRACKET Declare_var BODY RBRACKET SEMICOLON'

def p_action_4(p):
    'ACTION_4 :'
    # 4.- Add functions to D_Functions
    d_functions.add_function(p[-1],"void")
    
def p_Parameters(p):
    '''Parameters : ID ACTION_2 COLON Type More_parameters
                  | vacio'''


def p_More_parameters(p):
    '''More_parameters : COMMA Parameters
                      | vacio'''

def p_BODY(p):
    'BODY : LCBRACKET Declare_statement RCBRACKET'

def p_Declare_statement(p):
    '''Declare_statement : STATEMENT Declare_statement
                         | vacio'''

def p_STATEMENT(p):
    '''STATEMENT : ASSIGN
                 | CONDITION
                 | CYCLE
                 | F_CALL
                 | PRINTF'''


def p_ASSIGN(p):
    'ASSIGN : ID EQUALS EXPRESION SEMICOLON'

def p_EXPRESION(p):
    'EXPRESION : EXP Comp_logic'

def p_Comp_logic(p):
    '''Comp_logic : Op_logic EXP
                  | vacio'''

def p_Op_logic(p):
    '''Op_logic : GREATER
                | LESS
                | NOT_EQUALS'''

def p_EXP(p):
    'EXP : TERMINO Sum_res'

def p_Sum_res(p):
    '''Sum_res : PLUS EXP
               | MINUS EXP
               | vacio'''

def p_TERMINO(p):
    'TERMINO : FACTOR Mult_div'

def p_Mult_div(p):
    '''Mult_div : MULTIPLICATION TERMINO
                | DIVISION TERMINO
                | vacio'''

def p_FACTOR(p):
    '''FACTOR : LPARENTHESES EXPRESION RPARENTHESES
              | Sum_res_factor ID_CONST'''


def p_Sum_res_factor(p):
    '''Sum_res_factor : PLUS
                      | MINUS
                      | vacio'''

def p_ID_CONST(p):
    '''ID_CONST : ID
                | CTE'''

def p_CTE(p):
    '''CTE : CTE_INT
           | CTE_FLOAT'''

def p_PRINTF(p):
    'PRINTF : PRINT LPARENTHESES List_expresions RPARENTHESES SEMICOLON'

def p_List_expresions(p):
    'List_expresions : Opt_exp More_expresions'

def p_Opt_exp(p):
    '''Opt_exp : EXPRESION
               | CTE_STRING'''

def p_more_expresions(p):
    '''More_expresions : COMMA List_expresions
                       | vacio'''

def p_CYCLE(p):
    'CYCLE : DO  BODY WHILE LPARENTHESES EXPRESION RPARENTHESES SEMICOLON'

def p_CONDITION(p):
    'CONDITION : IF LPARENTHESES EXPRESION RPARENTHESES BODY Else_condition SEMICOLON'

def p_Else_condition(p):
    '''Else_condition : ELSE BODY
                      | vacio'''

def p_F_call(p):
    'F_CALL : ID LPARENTHESES F_expresion RPARENTHESES SEMICOLON'

def p_F_expresion(p):
    '''F_expresion : List_fexpresions
                   | vacio'''

def p_List_fexpresions(p):
    'List_fexpresions : EXPRESION More_fexpresions'

def p_More_fexpresions(p):
    '''More_fexpresions : COMMA List_fexpresions
                        | vacio'''


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
   
# Empty rule 
def p_vacio(p):
    'vacio : '
    pass  




# Build the parser
parser = yacc.yacc()

