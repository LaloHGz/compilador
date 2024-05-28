import ply.yacc as yacc
from lexer import tokens
from sem import D_Functions, SEM, PilaO, Pila, Quadruples, MemoryManager, operation_codes

# Create Virtual Memory Manager
memory_manager = MemoryManager()

# Create the Functions Directory
d_functions = D_Functions(memory_manager)

# Create list of temporary ids
temp_ids = []

# Create PilaO
pila_o = PilaO()

# Create Poper
poper = Pila("operators")

# Create PSaltos
psaltos = Pila("jumps")

# Create list of Quadruples
quadruples = Quadruples(memory_manager)

# Parsing rules
def p_Programa(p):
    'Programa : PROGRAM ID ACTION_1 SEMICOLON Declare_var Declare_func MAIN BODY END FINAL_ACTION'

def p_final_actionn(p):
    'FINAL_ACTION :'
    d_functions.destroy()
    pila_o.destroy()
    poper.destroy()
    psaltos.destroy()
    
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
    'ASSIGN : ID ACTION_1_2_ID EQUALS ACTION_2_2 EXPRESION SEMICOLON ACTION_10_2'

def p_EXPRESION(p):
    'EXPRESION : EXP Comp_logic'

def p_Comp_logic(p):
    '''Comp_logic : Op_logic EXP ACTION_9_2
                  | vacio'''

def p_Op_logic(p):
    '''Op_logic : GREATER ACTION_8_2
                | LESS ACTION_8_2
                | NOT_EQUALS ACTION_8_2'''

def p_EXP(p):
    'EXP : TERMINO ACTION_4_2 Sum_res'

def p_Sum_res(p):
    '''Sum_res : PLUS ACTION_2_2 EXP
               | MINUS ACTION_2_2 EXP
               | vacio'''

def p_TERMINO(p):
    'TERMINO : FACTOR ACTION_5_2 Mult_div'

def p_Mult_div(p):
    '''Mult_div : MULTIPLICATION ACTION_3_2 TERMINO
                | DIVISION ACTION_3_2 TERMINO
                | vacio'''

def p_FACTOR(p):
    '''FACTOR : LPARENTHESES ACTION_6_2 EXPRESION RPARENTHESES ACTION_7_2
              | Sum_res_factor ID_CONST'''


def p_Sum_res_factor(p):
    '''Sum_res_factor : PLUS
                      | MINUS
                      | vacio'''

def p_ID_CONST(p):
    '''ID_CONST : ID ACTION_1_2_ID
                | CTE'''
                
def p_CTE(p):
    '''CTE : CTE_INT ACTION_1_2_INT
           | CTE_FLOAT ACTION_1_2_FLOAT'''

def p_action_1_2_id(p):
    'ACTION_1_2_ID :'
    pila_o.push(d_functions.get_variable_address(p[-1]),d_functions.get_variable_type(p[-1]))
    
                
def p_action_1_2_int(p):
    'ACTION_1_2_INT :'
    pila_o.push(memory_manager.allocate('Ci',p[-1]),"int")
    
def p_action_1_2_float(p):
    'ACTION_1_2_FLOAT :'
    pila_o.push(memory_manager.allocate('Cf',p[-1]),"float")

def p_action_2_2(p):
    'ACTION_2_2 :'
    poper.push(operation_codes[p[-1]])
    
def p_action_3_2(p):
    'ACTION_3_2 :'
    poper.push(operation_codes[p[-1]])
    
def p_action_4_2(p):
    'ACTION_4_2 :'
    if(poper.top() == operation_codes["+"] or poper.top() == operation_codes["-"]):
        right_op, right_type = pila_o.pop()
        left_op, left_type = pila_o.pop()
        operator = poper.pop()
        result_type = SEM[operator][left_type][right_type]
        if(result_type != "error"):
            quadruples.add_entry(operator,left_op,right_op,-1,result_type)
            last_result = quadruples.get_last_result()
            pila_o.push(last_result,result_type)
        else:
            raise ValueError("Type mismatch")
            
def p_action_5_2(p):
    'ACTION_5_2 :'
    if(poper.top() == operation_codes["*"] or poper.top() == operation_codes["/"]):
        right_op, right_type = pila_o.pop()
        left_op, left_type = pila_o.pop()
        operator = poper.pop()
        result_type = SEM[operator][left_type][right_type]
        if(result_type != "error"):
            quadruples.add_entry(operator,left_op,right_op,-1,result_type)
            last_result = quadruples.get_last_result()
            pila_o.push(last_result,result_type)
        else:
            raise ValueError("Type mismatch")

def p_action_6_2(p):
    'ACTION_6_2 :'
    poper.push("(")

def p_action_7_2(p):
    'ACTION_7_2 :'
    poper.pop()
    
def p_action_8_2(p):
    'ACTION_8_2 :'
    poper.push(operation_codes[p[-1]])
    
def p_action_9_2(p):
    'ACTION_9_2 :'
    if(poper.top() == operation_codes[">"] or poper.top() == operation_codes["<"] or poper.top() == operation_codes["!="]):
        right_op, right_type = pila_o.pop()
        left_op, left_type = pila_o.pop()
        operator = poper.pop()
        result_type = SEM[operator][left_type][right_type]
        if(result_type != "error"):
            quadruples.add_entry(operator,left_op,right_op,-1, result_type)
            last_result = quadruples.get_last_result()
            pila_o.push(last_result,result_type)
        else:
            raise ValueError("Type mismatch")

    
def p_action_10_2(p):
    'ACTION_10_2 :'
    right_op, right_type = pila_o.pop()
    left_op, left_type = pila_o.pop()
    operator = poper.pop()
    result_type = SEM[operator][left_type][right_type]
    if(result_type != "error"):
        quadruples.add_entry(operator,right_op,-1,left_op)
        last_result = quadruples.get_last_result()
        pila_o.push(last_result,result_type)
    else:
        raise ValueError("Type mismatch")


def p_PRINTF(p):
    'PRINTF : PRINT LPARENTHESES List_expresions RPARENTHESES SEMICOLON'

def p_List_expresions(p):
    'List_expresions : Opt_exp ACTION_2_PRINT More_expresions'

def p_Opt_exp(p):
    '''Opt_exp : EXPRESION
               | CTE_STRING ACTION_1_PRINT'''

def p_more_expresions(p):
    '''More_expresions : COMMA List_expresions
                       | vacio'''
                       
def p_action_1_print(p):
    'ACTION_1_PRINT :'
    pila_o.push(memory_manager.allocate('Cs',p[-1]),"string")
    
def p_action_2_print(p):
    'ACTION_2_PRINT :'
    elem, elem_type = pila_o.pop()
    quadruples.add_entry(operation_codes["print"],-1,-1,elem)
    

def p_CYCLE(p):
    'CYCLE : DO ACTION_1_DW BODY WHILE LPARENTHESES EXPRESION RPARENTHESES SEMICOLON ACTION_2_DW'

def p_action_1_dw(p):
    'ACTION_1_DW :'
    psaltos.push(quadruples.size())
    
def p_action_2_dw(p):
    'ACTION_2_DW :'
    cond, cond_type = pila_o.pop()
    if(cond_type == "bool"):
        retorno = psaltos.pop()
        quadruples.add_entry(operation_codes["gotoV"],cond, -1,retorno)
    else:
        raise ValueError("Type mismatch condition type: ",cond_type,", expected bool")

def p_CONDITION(p):
    'CONDITION : IF LPARENTHESES EXPRESION RPARENTHESES ACTION_1_IF BODY Else_condition SEMICOLON ACTION_2_IF'

def p_Else_condition(p):
    '''Else_condition : ELSE ACTION_3_IF BODY
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

def p_action_1_if(p):
    'ACTION_1_IF :'
    result, exp_type = pila_o.pop()
    if(exp_type != "bool"):
        raise ValueError("Type Mismatch")
    else:
        quadruples.add_entry(operation_codes["gotoF"],result)
        psaltos.push(quadruples.size()-1)
        
def p_action_2_if(p):
    'ACTION_2_IF :'
    end = psaltos.pop()
    quadruples.update_result(end,quadruples.size())
    
def p_action_3_if(p):
    'ACTION_3_IF :'
    quadruples.add_entry(operation_codes["goto"])
    _false = psaltos.pop()
    psaltos.push(quadruples.size()-1)
    quadruples.update_result(_false,quadruples.size())

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
   
# Empty rule 
def p_vacio(p):
    'vacio : '
    pass  




# Build the parser
parser = yacc.yacc()

