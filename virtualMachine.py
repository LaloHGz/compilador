from main import compile
from parser_1 import quadruples, memory_manager
from tests import tests  # Import test cases

def run_test_case(case_number):
    # Run compiler with Test number
    compile(case_number)

    ip = 0 # Instruction pointer

    # Function to do the operations
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
            case '>':
                result = left > right
            case '<':
                result = left < right
            case '!=':
                result = left != right
        memory_manager.set_value(quadruples[ip]['result'],result)


    # Read Code
    while(ip < quadruples.size()):
        match quadruples[ip]['action']:
            case 1:
                # sum (+)
                operation('+',ip)
                ip += 1
                
            case 2:
                # minus (-)
                operation('-',ip)
                ip += 1
                
            case 3:
                # multiplication (*)
                operation('*',ip)
                ip += 1
                
            case 4:
                # division (/)
                operation('/',ip)
                ip += 1
                
            case 5:
                # equals (=)
                result = memory_manager.get_value(quadruples[ip]['left_side'])
                memory_manager.set_value(quadruples[ip]['result'], result)
                ip += 1
                
            case 6:
                # greater (>)
                operation('>',ip)
                ip += 1
                
            case 7:
                # less (<)
                operation('<',ip)
                ip += 1
                
            case 8:
                # not equals (!=)
                operation('!=',ip)
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

    # Llamar a destroy en todas las clases
    memory_manager.destroy()
    quadruples.destroy()
  
  
for i in range(0,24):
    print("Test Case #",i)
    run_test_case(i)  
    print("\n-------------------------------")
