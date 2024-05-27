from main import testCase
from parser_1 import quadruples, memory_manager

# Run compiler with Test number
testCase(9)

ip = 0 # Instruction pointer

'''
operation_codes = { '+': 1,
                    '-': 2,
                    '*': 3,
                    '/': 4,
                    '=': 5,
                    '>': 6,
                    '<': 7,
                    '!=': 8,
                    'print': 9,
                    'gotoF': 10,
                    'gotoV': 11,
                    'goto': 12}
'''

while(ip < quadruples.size()):
    match quadruples[ip]['action']:
        case 1:
            # sum (+)
            left = memory_manager.get_value(quadruples[ip]['left_side'])
            right = memory_manager.get_value(quadruples[ip]['right_side'])
            result = left + right
            memory_manager.set_value(quadruples[ip]['result'],result)
            ip += 1
            
        case 2:
            # minus (-)
            left = memory_manager.get_value(quadruples[ip]['left_side'])
            right = memory_manager.get_value(quadruples[ip]['right_side'])
            result = left - right
            memory_manager.set_value(quadruples[ip]['result'],result)
            ip += 1
            
        case 3:
            # multiplication (*)
            left = memory_manager.get_value(quadruples[ip]['left_side'])
            right = memory_manager.get_value(quadruples[ip]['right_side'])
            result = left * right
            memory_manager.set_value(quadruples[ip]['result'],result)
            ip += 1
            
        case 4:
            # division (/)
            left = memory_manager.get_value(quadruples[ip]['left_side'])
            right = memory_manager.get_value(quadruples[ip]['right_side'])
            result = left / right
            memory_manager.set_value(quadruples[ip]['result'],result)
            ip += 1
            
        case 5:
            # equals (=)
            result = memory_manager.get_value(quadruples[ip]['left_side'])
            memory_manager.set_value(quadruples[ip]['result'], result)
            ip += 1
            
        case 6:
            # greater (>)
            left = memory_manager.get_value(quadruples[ip]['left_side'])
            right = memory_manager.get_value(quadruples[ip]['right_side'])
            result = left > right
            memory_manager.set_value(quadruples[ip]['result'],result)  
            ip += 1
            
        case 7:
            # less (<)
            left = memory_manager.get_value(quadruples[ip]['left_side'])
            right = memory_manager.get_value(quadruples[ip]['right_side'])
            result = left < right
            memory_manager.set_value(quadruples[ip]['result'],result)
            ip += 1
            
        case 8:
            # not equals (!=)
            left = memory_manager.get_value(quadruples[ip]['left_side'])
            right = memory_manager.get_value(quadruples[ip]['right_side'])
            result = left != right
            memory_manager.set_value(quadruples[ip]['result'],result)
            ip += 1
            
        case 9:
            # print
            value = memory_manager.get_value(quadruples[ip]['result'])
            print(value)
            ip += 1
            
        case 10:
            # gotoF
            exp = memory_manager.get_value(quadruples[ip]['left_side'])
            if(exp):
                ip +=1
            else:
                ip = quadruples[ip]['result']
                
        case 11:
            # gotoV
            exp = memory_manager.get_value(quadruples[ip]['left_side'])
            if(exp):
                ip = quadruples[ip]['result']
            else:
                ip +=1
            
        case 12:
            # goto
            ip = quadruples[ip]['result']
            

def operation(op, ip):
    left = memory_manager.get_value(quadruples[ip]['left_side'])
    right = memory_manager.get_value(quadruples[ip]['right_side'])
    match op:
        case '+':
            result = left + right
        case '-':
            result = left - right
        case '*':
            result = left * right
        case '/':
            result = left / right
    memory_manager.set_value(quadruples[ip]['result'],result)