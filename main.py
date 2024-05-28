from lexer import lexer
from parser_1 import parser
from tests import tests  # Import test cases

# compile test case number
def compile(n):
    lexer.input(tests[n])
    parser.parse(tests[n])
