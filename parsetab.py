
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMMA CTE_FLOAT CTE_INT CTE_STRING DIVISION DO ELSE END EQUALS FLOAT GREATER ID IF INT LBRACKET LCBRACKET LESS LPARENTHESES MAIN MINUS MULTIPLICATION NOT_EQUALS PLUS PRINT PROGRAM RBRACKET RCBRACKET RPARENTHESES SEMICOLON VAR VOID WHILEPrograma : PROGRAM ID SEMICOLON Declare_var Declare_func MAIN BODY ENDDeclare_var : VARS\n                   | vacioVARS : VAR VariablesVariables : List_ids COLON Type SEMICOLON More_variablesMore_variables : Variables\n                      | vacioList_ids : ID More_idsMore_ids : COMMA List_ids\n                | vacioType : INT\n            | FLOATDeclare_func : FUNCS More_func\n                    | vacioMore_func : Declare_func\n                 | vacioFUNCS : VOID ID LPARENTHESES Parameters RPARENTHESES LBRACKET Declare_var BODY RBRACKET SEMICOLONParameters : ID COLON Type More_parameters\n                  | vacioMore_parameters : COMMA Parameters\n                      | vacioBODY : LCBRACKET Declare_statement RCBRACKETDeclare_statement : STATEMENT Declare_statement\n                         | vacioSTATEMENT : ASSIGN\n                 | CONDITION\n                 | CYCLE\n                 | F_CALL\n                 | PRINTFASSIGN : ID EQUALS EXPRESION SEMICOLONEXPRESION : EXP Comp_logicComp_logic : Op_logic EXP\n                  | vacioOp_logic : GREATER\n                | LESS\n                | NOT_EQUALSEXP : TERMINO Sum_resSum_res : PLUS EXP\n               | MINUS EXP\n               | vacioTERMINO : FACTOR Mult_divMult_div : MULTIPLICATION TERMINO\n                | DIVISION TERMINO\n                | vacioFACTOR : LPARENTHESES EXPRESION RPARENTHESES\n              | Sum_res_factor ID_CONSTSum_res_factor : PLUS\n                      | MINUS\n                      | vacioID_CONST : ID\n                | CTECTE : CTE_INT\n           | CTE_FLOATPRINTF : PRINT LPARENTHESES List_expresions RPARENTHESES SEMICOLONList_expresions : Opt_exp More_expresionsOpt_exp : EXPRESION\n               | CTE_STRINGMore_expresions : COMMA List_expresions\n                       | vacioCYCLE : DO  BODY WHILE LPARENTHESES EXPRESION RPARENTHESES SEMICOLONCONDITION : IF LPARENTHESES EXPRESION RPARENTHESES BODY Else_condition SEMICOLONElse_condition : ELSE BODY\n                      | vacioF_CALL : ID LPARENTHESES F_expresion RPARENTHESES SEMICOLONF_expresion : List_fexpresions\n                   | vacioList_fexpresions : EXPRESION More_fexpresionsMore_fexpresions : COMMA List_fexpresions\n                        | vaciovacio : '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,32,],[0,-1,]),'ID':([2,8,12,23,26,27,34,36,37,38,39,40,48,51,52,53,55,65,66,67,68,69,72,82,84,86,87,88,90,91,94,95,105,108,111,114,123,127,136,138,],[3,15,20,15,41,45,41,-25,-26,-27,-28,-29,15,-70,-70,-70,-70,-70,99,-47,-48,-49,-49,-30,-70,-34,-35,-36,-70,-70,-70,-70,-70,-70,-70,45,-64,-54,-61,-60,]),'SEMICOLON':([3,28,29,30,49,61,62,63,64,83,85,89,92,93,96,98,99,100,101,102,103,109,117,118,119,120,121,122,125,131,133,134,135,137,],[4,48,-11,-12,-22,82,-70,-70,-70,-31,-33,-37,-40,-41,-44,-46,-50,-51,-52,-53,123,127,-32,-38,-39,-42,-43,-45,-70,136,-63,138,139,-62,]),'VAR':([4,81,],[8,8,]),'VOID':([4,5,6,7,10,13,48,58,59,60,139,],[-70,12,-2,-3,12,-4,-70,-5,-6,-7,-17,]),'MAIN':([4,5,6,7,9,10,11,13,17,18,19,48,58,59,60,139,],[-70,-70,-2,-3,16,-70,-14,-4,-13,-15,-14,-70,-5,-6,-7,-17,]),'LCBRACKET':([6,7,13,16,43,48,58,59,60,81,107,116,132,],[-2,-3,-4,26,26,-70,-5,-6,-7,-70,26,26,26,]),'COLON':([14,15,22,24,31,45,],[21,-70,-8,-10,-9,56,]),'COMMA':([15,29,30,62,63,64,73,77,78,79,80,83,85,89,92,93,96,98,99,100,101,102,117,118,119,120,121,122,],[23,-11,-12,-70,-70,-70,105,111,-56,-57,114,-31,-33,-37,-40,-41,-44,-46,-50,-51,-52,-53,-32,-38,-39,-42,-43,-45,]),'LPARENTHESES':([20,41,42,44,51,52,53,55,65,75,84,86,87,88,90,91,94,95,105,108,111,],[27,52,53,55,65,65,65,65,65,108,65,-34,-35,-36,65,65,65,65,65,65,65,]),'INT':([21,56,],[29,29,]),'FLOAT':([21,56,],[30,30,]),'END':([25,49,],[32,-22,]),'RCBRACKET':([26,33,34,35,36,37,38,39,40,50,82,123,127,136,138,],[-70,49,-70,-24,-25,-26,-27,-28,-29,-23,-30,-64,-54,-61,-60,]),'IF':([26,34,36,37,38,39,40,82,123,127,136,138,],[42,42,-25,-26,-27,-28,-29,-30,-64,-54,-61,-60,]),'DO':([26,34,36,37,38,39,40,82,123,127,136,138,],[43,43,-25,-26,-27,-28,-29,-30,-64,-54,-61,-60,]),'PRINT':([26,34,36,37,38,39,40,82,123,127,136,138,],[44,44,-25,-26,-27,-28,-29,-30,-64,-54,-61,-60,]),'RPARENTHESES':([27,29,30,46,47,52,62,63,64,70,71,72,73,74,76,77,78,79,80,83,85,89,92,93,96,97,98,99,100,101,102,104,106,110,112,113,114,115,117,118,119,120,121,122,124,126,128,129,],[-70,-11,-12,57,-19,-70,-70,-70,-70,103,-65,-66,-70,107,109,-70,-56,-57,-70,-31,-33,-37,-40,-41,-44,122,-46,-50,-51,-52,-53,-67,-69,-55,-59,-18,-70,-21,-32,-38,-39,-42,-43,-45,-68,134,-58,-20,]),'EQUALS':([41,],[51,]),'WHILE':([49,54,],[-22,75,]),'ELSE':([49,125,],[-22,132,]),'RBRACKET':([49,130,],[-22,135,]),'PLUS':([51,52,53,55,63,64,65,84,86,87,88,90,91,93,94,95,96,98,99,100,101,102,105,108,111,120,121,122,],[67,67,67,67,90,-70,67,67,-34,-35,-36,67,67,-41,67,67,-44,-46,-50,-51,-52,-53,67,67,67,-42,-43,-45,]),'MINUS':([51,52,53,55,63,64,65,84,86,87,88,90,91,93,94,95,96,98,99,100,101,102,105,108,111,120,121,122,],[68,68,68,68,91,-70,68,68,-34,-35,-36,68,68,-41,68,68,-44,-46,-50,-51,-52,-53,68,68,68,-42,-43,-45,]),'CTE_INT':([51,52,53,55,65,66,67,68,69,72,84,86,87,88,90,91,94,95,105,108,111,],[-70,-70,-70,-70,-70,101,-47,-48,-49,-49,-70,-34,-35,-36,-70,-70,-70,-70,-70,-70,-70,]),'CTE_FLOAT':([51,52,53,55,65,66,67,68,69,72,84,86,87,88,90,91,94,95,105,108,111,],[-70,-70,-70,-70,-70,102,-47,-48,-49,-49,-70,-34,-35,-36,-70,-70,-70,-70,-70,-70,-70,]),'CTE_STRING':([55,111,],[79,79,]),'LBRACKET':([57,],[81,]),'GREATER':([62,63,64,89,92,93,96,98,99,100,101,102,118,119,120,121,122,],[86,-70,-70,-37,-40,-41,-44,-46,-50,-51,-52,-53,-38,-39,-42,-43,-45,]),'LESS':([62,63,64,89,92,93,96,98,99,100,101,102,118,119,120,121,122,],[87,-70,-70,-37,-40,-41,-44,-46,-50,-51,-52,-53,-38,-39,-42,-43,-45,]),'NOT_EQUALS':([62,63,64,89,92,93,96,98,99,100,101,102,118,119,120,121,122,],[88,-70,-70,-37,-40,-41,-44,-46,-50,-51,-52,-53,-38,-39,-42,-43,-45,]),'MULTIPLICATION':([64,98,99,100,101,102,122,],[94,-46,-50,-51,-52,-53,-45,]),'DIVISION':([64,98,99,100,101,102,122,],[95,-46,-50,-51,-52,-53,-45,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Programa':([0,],[1,]),'Declare_var':([4,81,],[5,116,]),'VARS':([4,81,],[6,6,]),'vacio':([4,5,10,15,26,27,34,48,51,52,53,55,62,63,64,65,73,77,80,81,84,90,91,94,95,105,108,111,114,125,],[7,11,19,24,35,47,35,60,69,72,69,69,85,92,96,69,106,112,115,7,69,69,69,69,69,69,69,69,47,133,]),'Declare_func':([5,10,],[9,18,]),'FUNCS':([5,10,],[10,10,]),'Variables':([8,48,],[13,59,]),'List_ids':([8,23,48,],[14,31,14,]),'More_func':([10,],[17,]),'More_ids':([15,],[22,]),'BODY':([16,43,107,116,132,],[25,54,125,130,137,]),'Type':([21,56,],[28,80,]),'Declare_statement':([26,34,],[33,50,]),'STATEMENT':([26,34,],[34,34,]),'ASSIGN':([26,34,],[36,36,]),'CONDITION':([26,34,],[37,37,]),'CYCLE':([26,34,],[38,38,]),'F_CALL':([26,34,],[39,39,]),'PRINTF':([26,34,],[40,40,]),'Parameters':([27,114,],[46,129,]),'More_variables':([48,],[58,]),'EXPRESION':([51,52,53,55,65,105,108,111,],[61,73,74,78,97,73,126,78,]),'EXP':([51,52,53,55,65,84,90,91,105,108,111,],[62,62,62,62,62,117,118,119,62,62,62,]),'TERMINO':([51,52,53,55,65,84,90,91,94,95,105,108,111,],[63,63,63,63,63,63,63,63,120,121,63,63,63,]),'FACTOR':([51,52,53,55,65,84,90,91,94,95,105,108,111,],[64,64,64,64,64,64,64,64,64,64,64,64,64,]),'Sum_res_factor':([51,52,53,55,65,84,90,91,94,95,105,108,111,],[66,66,66,66,66,66,66,66,66,66,66,66,66,]),'F_expresion':([52,],[70,]),'List_fexpresions':([52,105,],[71,124,]),'List_expresions':([55,111,],[76,128,]),'Opt_exp':([55,111,],[77,77,]),'Comp_logic':([62,],[83,]),'Op_logic':([62,],[84,]),'Sum_res':([63,],[89,]),'Mult_div':([64,],[93,]),'ID_CONST':([66,],[98,]),'CTE':([66,],[100,]),'More_fexpresions':([73,],[104,]),'More_expresions':([77,],[110,]),'More_parameters':([80,],[113,]),'Else_condition':([125,],[131,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Programa","S'",1,None,None,None),
  ('Programa -> PROGRAM ID SEMICOLON Declare_var Declare_func MAIN BODY END','Programa',8,'p_Programa','parser.py',9),
  ('Declare_var -> VARS','Declare_var',1,'p_Declare_var','parser.py',13),
  ('Declare_var -> vacio','Declare_var',1,'p_Declare_var','parser.py',14),
  ('VARS -> VAR Variables','VARS',2,'p_VARS','parser.py',17),
  ('Variables -> List_ids COLON Type SEMICOLON More_variables','Variables',5,'p_Variables','parser.py',20),
  ('More_variables -> Variables','More_variables',1,'p_More_variables','parser.py',23),
  ('More_variables -> vacio','More_variables',1,'p_More_variables','parser.py',24),
  ('List_ids -> ID More_ids','List_ids',2,'p_List_ids','parser.py',27),
  ('More_ids -> COMMA List_ids','More_ids',2,'p_More_ids','parser.py',30),
  ('More_ids -> vacio','More_ids',1,'p_More_ids','parser.py',31),
  ('Type -> INT','Type',1,'p_Type','parser.py',34),
  ('Type -> FLOAT','Type',1,'p_Type','parser.py',35),
  ('Declare_func -> FUNCS More_func','Declare_func',2,'p_Declare_func','parser.py',38),
  ('Declare_func -> vacio','Declare_func',1,'p_Declare_func','parser.py',39),
  ('More_func -> Declare_func','More_func',1,'p_More_func','parser.py',42),
  ('More_func -> vacio','More_func',1,'p_More_func','parser.py',43),
  ('FUNCS -> VOID ID LPARENTHESES Parameters RPARENTHESES LBRACKET Declare_var BODY RBRACKET SEMICOLON','FUNCS',10,'p_FUNCS','parser.py',46),
  ('Parameters -> ID COLON Type More_parameters','Parameters',4,'p_Parameters','parser.py',49),
  ('Parameters -> vacio','Parameters',1,'p_Parameters','parser.py',50),
  ('More_parameters -> COMMA Parameters','More_parameters',2,'p_More_parameters','parser.py',53),
  ('More_parameters -> vacio','More_parameters',1,'p_More_parameters','parser.py',54),
  ('BODY -> LCBRACKET Declare_statement RCBRACKET','BODY',3,'p_BODY','parser.py',57),
  ('Declare_statement -> STATEMENT Declare_statement','Declare_statement',2,'p_Declare_statement','parser.py',60),
  ('Declare_statement -> vacio','Declare_statement',1,'p_Declare_statement','parser.py',61),
  ('STATEMENT -> ASSIGN','STATEMENT',1,'p_STATEMENT','parser.py',64),
  ('STATEMENT -> CONDITION','STATEMENT',1,'p_STATEMENT','parser.py',65),
  ('STATEMENT -> CYCLE','STATEMENT',1,'p_STATEMENT','parser.py',66),
  ('STATEMENT -> F_CALL','STATEMENT',1,'p_STATEMENT','parser.py',67),
  ('STATEMENT -> PRINTF','STATEMENT',1,'p_STATEMENT','parser.py',68),
  ('ASSIGN -> ID EQUALS EXPRESION SEMICOLON','ASSIGN',4,'p_ASSIGN','parser.py',72),
  ('EXPRESION -> EXP Comp_logic','EXPRESION',2,'p_EXPRESION','parser.py',75),
  ('Comp_logic -> Op_logic EXP','Comp_logic',2,'p_Comp_logic','parser.py',78),
  ('Comp_logic -> vacio','Comp_logic',1,'p_Comp_logic','parser.py',79),
  ('Op_logic -> GREATER','Op_logic',1,'p_Op_logic','parser.py',82),
  ('Op_logic -> LESS','Op_logic',1,'p_Op_logic','parser.py',83),
  ('Op_logic -> NOT_EQUALS','Op_logic',1,'p_Op_logic','parser.py',84),
  ('EXP -> TERMINO Sum_res','EXP',2,'p_EXP','parser.py',87),
  ('Sum_res -> PLUS EXP','Sum_res',2,'p_Sum_res','parser.py',90),
  ('Sum_res -> MINUS EXP','Sum_res',2,'p_Sum_res','parser.py',91),
  ('Sum_res -> vacio','Sum_res',1,'p_Sum_res','parser.py',92),
  ('TERMINO -> FACTOR Mult_div','TERMINO',2,'p_TERMINO','parser.py',95),
  ('Mult_div -> MULTIPLICATION TERMINO','Mult_div',2,'p_Mult_div','parser.py',98),
  ('Mult_div -> DIVISION TERMINO','Mult_div',2,'p_Mult_div','parser.py',99),
  ('Mult_div -> vacio','Mult_div',1,'p_Mult_div','parser.py',100),
  ('FACTOR -> LPARENTHESES EXPRESION RPARENTHESES','FACTOR',3,'p_FACTOR','parser.py',103),
  ('FACTOR -> Sum_res_factor ID_CONST','FACTOR',2,'p_FACTOR','parser.py',104),
  ('Sum_res_factor -> PLUS','Sum_res_factor',1,'p_Sum_res_factor','parser.py',108),
  ('Sum_res_factor -> MINUS','Sum_res_factor',1,'p_Sum_res_factor','parser.py',109),
  ('Sum_res_factor -> vacio','Sum_res_factor',1,'p_Sum_res_factor','parser.py',110),
  ('ID_CONST -> ID','ID_CONST',1,'p_ID_CONST','parser.py',113),
  ('ID_CONST -> CTE','ID_CONST',1,'p_ID_CONST','parser.py',114),
  ('CTE -> CTE_INT','CTE',1,'p_CTE','parser.py',117),
  ('CTE -> CTE_FLOAT','CTE',1,'p_CTE','parser.py',118),
  ('PRINTF -> PRINT LPARENTHESES List_expresions RPARENTHESES SEMICOLON','PRINTF',5,'p_PRINTF','parser.py',121),
  ('List_expresions -> Opt_exp More_expresions','List_expresions',2,'p_List_expresions','parser.py',124),
  ('Opt_exp -> EXPRESION','Opt_exp',1,'p_Opt_exp','parser.py',127),
  ('Opt_exp -> CTE_STRING','Opt_exp',1,'p_Opt_exp','parser.py',128),
  ('More_expresions -> COMMA List_expresions','More_expresions',2,'p_more_expresions','parser.py',131),
  ('More_expresions -> vacio','More_expresions',1,'p_more_expresions','parser.py',132),
  ('CYCLE -> DO BODY WHILE LPARENTHESES EXPRESION RPARENTHESES SEMICOLON','CYCLE',7,'p_CYCLE','parser.py',135),
  ('CONDITION -> IF LPARENTHESES EXPRESION RPARENTHESES BODY Else_condition SEMICOLON','CONDITION',7,'p_CONDITION','parser.py',138),
  ('Else_condition -> ELSE BODY','Else_condition',2,'p_Else_condition','parser.py',141),
  ('Else_condition -> vacio','Else_condition',1,'p_Else_condition','parser.py',142),
  ('F_CALL -> ID LPARENTHESES F_expresion RPARENTHESES SEMICOLON','F_CALL',5,'p_F_call','parser.py',145),
  ('F_expresion -> List_fexpresions','F_expresion',1,'p_F_expresion','parser.py',148),
  ('F_expresion -> vacio','F_expresion',1,'p_F_expresion','parser.py',149),
  ('List_fexpresions -> EXPRESION More_fexpresions','List_fexpresions',2,'p_List_fexpresions','parser.py',152),
  ('More_fexpresions -> COMMA List_fexpresions','More_fexpresions',2,'p_More_fexpresions','parser.py',155),
  ('More_fexpresions -> vacio','More_fexpresions',1,'p_More_fexpresions','parser.py',156),
  ('vacio -> <empty>','vacio',0,'p_vacio','parser.py',164),
]
