
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftSUMARESTAleftMULTIPLICACIONDIVISIONrightUMINUSASIGNACION CADENA DIFF DIVISION IGUAL IMPRIMIR INCRE LLAVE_D LLAVE_I MAYORQ MENORQ MIENTRAS MULTIPLICACION NUMERO PARA PARENTESIS_D PARENTESIS_I PUNTOCOMA RESTA SI SINO SUMA VARIABLEprogram : statement_liststatement_list : statement PUNTOCOMA\n| statement_list statement PUNTOCOMAstatement : VARIABLE ASIGNACION expressionstatement : expressionstatement : VARIABLE INCREstatement : SI PARENTESIS_I condicion PARENTESIS_D LLAVE_I statement_list LLAVE_Dstatement : SI PARENTESIS_I condicion PARENTESIS_D LLAVE_I statement_list LLAVE_D SINO LLAVE_I statement_list LLAVE_Dstatement : PARA PARENTESIS_I statement_list condicion PUNTOCOMA statement PARENTESIS_D LLAVE_I statement_list LLAVE_Dexpression : expression SUMA expression\n| expression RESTA expression\n| expression MULTIPLICACION expression\n| expression DIVISION expressionexpression : RESTA expression %prec UMINUSexpression : PARENTESIS_I expression PARENTESIS_Dexpression : NUMEROexpression : CADENAexpression : VARIABLEstatement : IMPRIMIR PARENTESIS_I expression PARENTESIS_Dcondicion : expression MAYORQ expression\n| expression MENORQ expression\n| expression IGUAL expression\n| expression DIFF expressionstatement : MIENTRAS PARENTESIS_I condicion PARENTESIS_D LLAVE_I statement_list LLAVE_D'
    
_lr_action_items = {'VARIABLE':([0,2,7,11,15,16,18,19,20,21,22,25,26,27,29,38,42,43,44,45,50,55,56,57,59,64,65,66,67,],[4,4,24,24,-2,24,24,24,24,24,24,4,24,24,-3,4,24,24,24,24,4,4,4,4,4,4,4,4,4,]),'SI':([0,2,15,25,29,38,50,55,56,57,59,64,65,66,67,],[6,6,-2,6,-3,6,6,6,6,6,6,6,6,6,6,]),'PARA':([0,2,15,25,29,38,50,55,56,57,59,64,65,66,67,],[8,8,-2,8,-3,8,8,8,8,8,8,8,8,8,8,]),'IMPRIMIR':([0,2,15,25,29,38,50,55,56,57,59,64,65,66,67,],[9,9,-2,9,-3,9,9,9,9,9,9,9,9,9,9,]),'MIENTRAS':([0,2,15,25,29,38,50,55,56,57,59,64,65,66,67,],[10,10,-2,10,-3,10,10,10,10,10,10,10,10,10,10,]),'RESTA':([0,2,4,5,7,11,12,13,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,42,43,44,45,47,50,51,52,53,54,55,56,57,59,64,65,66,67,],[11,11,-18,19,11,11,-16,-17,-2,11,11,11,11,11,11,19,-18,11,11,11,-14,-3,19,-10,-11,-12,-13,19,-15,11,19,11,11,11,11,19,11,19,19,19,19,11,11,11,11,11,11,11,11,]),'PARENTESIS_I':([0,2,6,7,8,9,10,11,15,16,18,19,20,21,22,25,26,27,29,38,42,43,44,45,50,55,56,57,59,64,65,66,67,],[7,7,22,7,25,26,27,7,-2,7,7,7,7,7,7,7,7,7,-3,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'NUMERO':([0,2,7,11,15,16,18,19,20,21,22,25,26,27,29,38,42,43,44,45,50,55,56,57,59,64,65,66,67,],[12,12,12,12,-2,12,12,12,12,12,12,12,12,12,-3,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'CADENA':([0,2,7,11,15,16,18,19,20,21,22,25,26,27,29,38,42,43,44,45,50,55,56,57,59,64,65,66,67,],[13,13,13,13,-2,13,13,13,13,13,13,13,13,13,-3,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'$end':([1,2,15,29,],[0,-1,-2,-3,]),'PUNTOCOMA':([3,4,5,12,13,14,17,24,28,30,31,32,33,34,37,46,47,48,51,52,53,54,60,62,68,69,],[15,-18,-5,-16,-17,29,-6,-18,-14,-4,-10,-11,-12,-13,-15,55,-5,-19,-20,-21,-22,-23,-7,-24,-9,-8,]),'ASIGNACION':([4,],[16,]),'INCRE':([4,],[17,]),'SUMA':([4,5,12,13,23,24,28,30,31,32,33,34,36,37,39,47,51,52,53,54,],[-18,18,-16,-17,18,-18,-14,18,-10,-11,-12,-13,18,-15,18,18,18,18,18,18,]),'MULTIPLICACION':([4,5,12,13,23,24,28,30,31,32,33,34,36,37,39,47,51,52,53,54,],[-18,20,-16,-17,20,-18,-14,20,20,20,-12,-13,20,-15,20,20,20,20,20,20,]),'DIVISION':([4,5,12,13,23,24,28,30,31,32,33,34,36,37,39,47,51,52,53,54,],[-18,21,-16,-17,21,-18,-14,21,21,21,-12,-13,21,-15,21,21,21,21,21,21,]),'MAYORQ':([4,12,13,24,28,31,32,33,34,36,37,47,],[-18,-16,-17,-18,-14,-10,-11,-12,-13,42,-15,42,]),'MENORQ':([4,12,13,24,28,31,32,33,34,36,37,47,],[-18,-16,-17,-18,-14,-10,-11,-12,-13,43,-15,43,]),'IGUAL':([4,12,13,24,28,31,32,33,34,36,37,47,],[-18,-16,-17,-18,-14,-10,-11,-12,-13,44,-15,44,]),'DIFF':([4,12,13,24,28,31,32,33,34,36,37,47,],[-18,-16,-17,-18,-14,-10,-11,-12,-13,45,-15,45,]),'PARENTESIS_D':([4,5,12,13,17,23,24,28,30,31,32,33,34,35,37,39,40,48,51,52,53,54,58,60,62,68,69,],[-18,-5,-16,-17,-6,37,-18,-14,-4,-10,-11,-12,-13,41,-15,48,49,-19,-20,-21,-22,-23,61,-7,-24,-9,-8,]),'LLAVE_D':([15,29,57,59,66,67,],[-2,-3,60,62,68,69,]),'LLAVE_I':([41,49,61,63,],[50,56,64,65,]),'SINO':([60,],[63,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,25,50,56,64,65,],[2,38,57,59,66,67,]),'statement':([0,2,25,38,50,55,56,57,59,64,65,66,67,],[3,14,3,14,3,58,3,14,14,3,3,14,14,]),'expression':([0,2,7,11,16,18,19,20,21,22,25,26,27,38,42,43,44,45,50,55,56,57,59,64,65,66,67,],[5,5,23,28,30,31,32,33,34,36,5,39,36,47,51,52,53,54,5,5,5,5,5,5,5,5,5,]),'condicion':([22,27,38,],[35,40,46,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','parser.py',13),
  ('statement_list -> statement PUNTOCOMA','statement_list',2,'p_statement_list','parser.py',17),
  ('statement_list -> statement_list statement PUNTOCOMA','statement_list',3,'p_statement_list','parser.py',18),
  ('statement -> VARIABLE ASIGNACION expression','statement',3,'p_statement_assign','parser.py',26),
  ('statement -> expression','statement',1,'p_statement_expr','parser.py',31),
  ('statement -> VARIABLE INCRE','statement',2,'p_statement_increment','parser.py',35),
  ('statement -> SI PARENTESIS_I condicion PARENTESIS_D LLAVE_I statement_list LLAVE_D','statement',7,'p_statement_if','parser.py',40),
  ('statement -> SI PARENTESIS_I condicion PARENTESIS_D LLAVE_I statement_list LLAVE_D SINO LLAVE_I statement_list LLAVE_D','statement',11,'p_statement_if_else','parser.py',45),
  ('statement -> PARA PARENTESIS_I statement_list condicion PUNTOCOMA statement PARENTESIS_D LLAVE_I statement_list LLAVE_D','statement',10,'p_statement_for','parser.py',50),
  ('expression -> expression SUMA expression','expression',3,'p_expression_binop','parser.py',54),
  ('expression -> expression RESTA expression','expression',3,'p_expression_binop','parser.py',55),
  ('expression -> expression MULTIPLICACION expression','expression',3,'p_expression_binop','parser.py',56),
  ('expression -> expression DIVISION expression','expression',3,'p_expression_binop','parser.py',57),
  ('expression -> RESTA expression','expression',2,'p_expression_uminus','parser.py',61),
  ('expression -> PARENTESIS_I expression PARENTESIS_D','expression',3,'p_expression_group','parser.py',65),
  ('expression -> NUMERO','expression',1,'p_expression_number','parser.py',69),
  ('expression -> CADENA','expression',1,'p_expression_string','parser.py',73),
  ('expression -> VARIABLE','expression',1,'p_expression_variable','parser.py',77),
  ('statement -> IMPRIMIR PARENTESIS_I expression PARENTESIS_D','statement',4,'p_print_statement','parser.py',81),
  ('condicion -> expression MAYORQ expression','condicion',3,'p_condicion','parser.py',85),
  ('condicion -> expression MENORQ expression','condicion',3,'p_condicion','parser.py',86),
  ('condicion -> expression IGUAL expression','condicion',3,'p_condicion','parser.py',87),
  ('condicion -> expression DIFF expression','condicion',3,'p_condicion','parser.py',88),
  ('statement -> MIENTRAS PARENTESIS_I condicion PARENTESIS_D LLAVE_I statement_list LLAVE_D','statement',7,'p_mientras','parser.py',92),
]
