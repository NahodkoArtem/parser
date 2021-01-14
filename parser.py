import sys
from lark import Lark
from lark.tree import pydot__tree_to_png

try:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
except IndexError:
    print("Входные параметры заданы некорректно!")
    exit(0)

grammar = r"""
    start: expr

    ?expr: factor_or
    ?factor_or: (factor_and "||")* factor_and
    ?factor_and: (factor_compare "&&")* factor_compare
    ?factor_compare: factor_not (_comp_op factor_not)*
    !?factor_not: "--" factor_sum_dif -> factor_not
        | factor_sum_dif
    ?factor_sum_dif: factor_mul_div (_add_op factor_mul_div)*
    ?factor_mul_div: term (_mul_op term)*
    ?term: _factor_op term | pow
    ?pow: func_expression ("**" term)?
    ?func_expression: func_expression "(" [args] ")" -> funccall
              | atom
    ?atom: IDENTIFIER -> var
         | NUMBER -> number
         | "(" expr ")"
    args: argvalue ("," argvalue)*
    ?argvalue: expr?
    
    !_factor_op: "-"
    !_add_op: "+"|"-"
    !_mul_op: "*"|"/"
    MUL: "*"
    DIV: "/"
    ADD: "+"
    SUB: "-"
    LT: "<"
    LTE: "<="
    GT: ">"
    GTE: ">="
    NEQ: "/="
    EQ: "=="
    !_comp_op: "<"|">"|"=="|">="|"<="|"/="
    
    NUMBER: /(0|[1-9][0-9]*)/
    IDENTIFIER: /[a-z]\w*/
    
    %import common.NEWLINE
    %import common.WS
    
    %ignore WS
    
"""

p = Lark(grammar)

if __name__ == '__main__':
    with open(input_file, "r") as file:
        try:
            code = file.read()
            tree = p.parse(code)
            pydot__tree_to_png(tree, output_file)
        except Exception as e:
            print(f"Parse error! {e}")
