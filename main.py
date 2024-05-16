from lexer import lexer
from parser_1 import parser,d_functions
from tests import tests  # Import test cases

# run test case number
def testCase(n):
    # Give the lexer some input
    lexer.input(tests[n])

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)

    parser.parse(tests[n], tracking = True, debug = True)
    
# run testCase n    
testCase(5)

print(d_functions.functions)

