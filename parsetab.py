
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftSUMARESTAleftMULTIPLICACIONDIVISIONrightUMINUSASIGNACION CADENA DIFF DIVISION IGUAL IMPRIMIR INCRE LLAVE_D LLAVE_I MAYORQ MENORQ MIENTRAS MULTIPLICACION NUMERO PARA PARENTESIS_D PARENTESIS_I PUNTOCOMA RESTA SI SINO SUMA VARIABLEprogram : statement_liststatement_list : statement PUNTOCOMA\n| statement_list statement PUNTOCOMAstatement : VARIABLE ASIGNACION expressionstatement : expressionstatement : VARIABLE INCREexpression : expression SUMA expression\n| expression RESTA expression\n| expression MULTIPLICACION expression\n| expression DIVISION expressionexpression : RESTA expression %prec UMINUSexpression : PARENTESIS_I expression PARENTESIS_Dexpression : NUMEROexpression : CADENAexpression : VARIABLEstatement : IMPRIMIR PARENTESIS_I expression PARENTESIS_Dcondicion : expression MAYORQ expression\n| expression MENORQ expression\n| expression IGUAL expression\n| expression DIFF expressionstatement : MIENTRAS PARENTESIS_I condicion PARENTESIS_D LLAVE_I statement_list LLAVE_D'
    
_lr_action_items = {'VARIABLE':([0,2,7,9,13,14,16,17,18,19,20,23,25,37,38,39,40,41,46,],[4,4,22,22,-2,22,22,22,22,22,22,22,-3,22,22,22,22,4,4,]),'IMPRIMIR':([0,2,13,25,41,46,],[6,6,-2,-3,6,6,]),'MIENTRAS':([0,2,13,25,41,46,],[8,8,-2,-3,8,8,]),'RESTA':([0,2,4,5,7,9,10,11,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,37,38,39,40,41,42,43,44,45,46,],[9,9,-15,17,9,9,-13,-14,-2,9,9,9,9,9,9,17,-15,9,-11,-3,17,-7,-8,-9,-10,17,-12,17,9,9,9,9,9,17,17,17,17,9,]),'PARENTESIS_I':([0,2,6,7,8,9,13,14,16,17,18,19,20,23,25,37,38,39,40,41,46,],[7,7,20,7,23,7,-2,7,7,7,7,7,7,7,-3,7,7,7,7,7,7,]),'NUMERO':([0,2,7,9,13,14,16,17,18,19,20,23,25,37,38,39,40,41,46,],[10,10,10,10,-2,10,10,10,10,10,10,10,-3,10,10,10,10,10,10,]),'CADENA':([0,2,7,9,13,14,16,17,18,19,20,23,25,37,38,39,40,41,46,],[11,11,11,11,-2,11,11,11,11,11,11,11,-3,11,11,11,11,11,11,]),'$end':([1,2,13,25,],[0,-1,-2,-3,]),'PUNTOCOMA':([3,4,5,10,11,12,15,22,24,26,27,28,29,30,32,35,47,],[13,-15,-5,-13,-14,25,-6,-15,-11,-4,-7,-8,-9,-10,-12,-16,-21,]),'ASIGNACION':([4,],[14,]),'INCRE':([4,],[15,]),'SUMA':([4,5,10,11,21,22,24,26,27,28,29,30,31,32,34,42,43,44,45,],[-15,16,-13,-14,16,-15,-11,16,-7,-8,-9,-10,16,-12,16,16,16,16,16,]),'MULTIPLICACION':([4,5,10,11,21,22,24,26,27,28,29,30,31,32,34,42,43,44,45,],[-15,18,-13,-14,18,-15,-11,18,18,18,-9,-10,18,-12,18,18,18,18,18,]),'DIVISION':([4,5,10,11,21,22,24,26,27,28,29,30,31,32,34,42,43,44,45,],[-15,19,-13,-14,19,-15,-11,19,19,19,-9,-10,19,-12,19,19,19,19,19,]),'PARENTESIS_D':([10,11,21,22,24,27,28,29,30,31,32,33,42,43,44,45,],[-13,-14,32,-15,-11,-7,-8,-9,-10,35,-12,36,-17,-18,-19,-20,]),'MAYORQ':([10,11,22,24,27,28,29,30,32,34,],[-13,-14,-15,-11,-7,-8,-9,-10,-12,37,]),'MENORQ':([10,11,22,24,27,28,29,30,32,34,],[-13,-14,-15,-11,-7,-8,-9,-10,-12,38,]),'IGUAL':([10,11,22,24,27,28,29,30,32,34,],[-13,-14,-15,-11,-7,-8,-9,-10,-12,39,]),'DIFF':([10,11,22,24,27,28,29,30,32,34,],[-13,-14,-15,-11,-7,-8,-9,-10,-12,40,]),'LLAVE_D':([13,25,46,],[-2,-3,47,]),'LLAVE_I':([36,],[41,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,41,],[2,46,]),'statement':([0,2,41,46,],[3,12,3,12,]),'expression':([0,2,7,9,14,16,17,18,19,20,23,37,38,39,40,41,46,],[5,5,21,24,26,27,28,29,30,31,34,42,43,44,45,5,5,]),'condicion':([23,],[33,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','parser.py',14),
  ('statement_list -> statement PUNTOCOMA','statement_list',2,'p_statement_list','parser.py',18),
  ('statement_list -> statement_list statement PUNTOCOMA','statement_list',3,'p_statement_list','parser.py',19),
  ('statement -> VARIABLE ASIGNACION expression','statement',3,'p_statement_assign','parser.py',27),
  ('statement -> expression','statement',1,'p_statement_expr','parser.py',32),
  ('statement -> VARIABLE INCRE','statement',2,'p_statement_increment','parser.py',36),
  ('expression -> expression SUMA expression','expression',3,'p_expression_binop','parser.py',40),
  ('expression -> expression RESTA expression','expression',3,'p_expression_binop','parser.py',41),
  ('expression -> expression MULTIPLICACION expression','expression',3,'p_expression_binop','parser.py',42),
  ('expression -> expression DIVISION expression','expression',3,'p_expression_binop','parser.py',43),
  ('expression -> RESTA expression','expression',2,'p_expression_uminus','parser.py',47),
  ('expression -> PARENTESIS_I expression PARENTESIS_D','expression',3,'p_expression_group','parser.py',51),
  ('expression -> NUMERO','expression',1,'p_expression_number','parser.py',55),
  ('expression -> CADENA','expression',1,'p_expression_string','parser.py',59),
  ('expression -> VARIABLE','expression',1,'p_expression_variable','parser.py',63),
  ('statement -> IMPRIMIR PARENTESIS_I expression PARENTESIS_D','statement',4,'p_print_statement','parser.py',67),
  ('condicion -> expression MAYORQ expression','condicion',3,'p_condicion','parser.py',71),
  ('condicion -> expression MENORQ expression','condicion',3,'p_condicion','parser.py',72),
  ('condicion -> expression IGUAL expression','condicion',3,'p_condicion','parser.py',73),
  ('condicion -> expression DIFF expression','condicion',3,'p_condicion','parser.py',74),
  ('statement -> MIENTRAS PARENTESIS_I condicion PARENTESIS_D LLAVE_I statement_list LLAVE_D','statement',7,'p_mientras','parser.py',78),
]
