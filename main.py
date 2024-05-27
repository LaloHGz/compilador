from lexer import lexer
from parser_1 import parser
from tests import tests  # Import test cases

# run test case number
def testCase(n):
    lexer.input(tests[n])
    parser.parse(tests[n])
