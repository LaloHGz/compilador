
# Creation of class to define the structure of D_Functions & D_Vars
class D_Functions:
    def __init__(self):
        self.functions = {}  # Dictionary to save all the functions
        self.current_function = None
        self.global_function = None  # Variable to store the global function name

    def add_function(self, function_name, function_type):
        if function_name not in self.functions:
            self.functions[function_name] = {'type': function_type, 'variables': {}}
            self.current_function = function_name
        else:
            raise ValueError("The function already exists.")
        
    def set_global_function(self, function_name):
        self.global_function = function_name

    def add_variable(self, variable_name, variable_type):
        if self.current_function is not None:
            if variable_name in self.functions[self.current_function]['variables']:
                raise ValueError("The variable already exists in the current function.")
            elif self.global_function is not None and self.global_function in self.functions and variable_name in self.functions[self.global_function]['variables']:
                raise ValueError("The variable already exists in the global scope.")
            else:
                self.functions[self.current_function]['variables'][variable_name] = variable_type
        else:
            raise ValueError("No current function selected.")

    def get_variable_type(self, variable_name):
        """
        Method to get the type of a variable by first looking in the current function's scope,
        and if not found, looking in the global function's scope.
        """
        # Check in the current function
        if self.current_function and variable_name in self.functions[self.current_function]['variables']:
            return self.functions[self.current_function]['variables'][variable_name]
        # Check in the global function
        elif self.global_function and variable_name in self.functions[self.global_function]['variables']:
            return self.functions[self.global_function]['variables'][variable_name]
        else:
            raise ValueError("Variable not found")  # Variable not found in either scope


# Stack PilaO class
class PilaO:
    def __init__(self):
        self.pila_operandos = []  # Stack to store operands
        self.pila_tipos = []       # Stack to store operand types

    def push(self, operando, tipo):
        """
        Method to add an operand and its type to the stacks.
        """
        self.pila_operandos.append(operando)
        self.pila_tipos.append(tipo)
        print(f"Added operand: {operando} with type: {tipo}")

    def pop(self):
        """
        Method to remove the last operand and its type from the stacks.
        """
        if not self.is_empty():
            operando = self.pila_operandos.pop()
            tipo = self.pila_tipos.pop()
            print(f"Removed operand: {operando} with type: {tipo}")
            return operando, tipo
        else:
            print("The stacks are empty")
            return None, None

    def top(self):
        """
        Method to get the last operand and its type without removing them from the stacks.
        """
        if not self.is_empty():
            operando = self.pila_operandos[-1]
            tipo = self.pila_tipos[-1]
            return operando, tipo
        else:
            print("The stacks are empty")
            return None, None

    def is_empty(self):
        """
        Method to check if the stacks are empty.
        """
        return len(self.pila_operandos) == 0 and len(self.pila_tipos) == 0

    def size(self):
        """
        Method to get the size of the stacks.
        """
        return len(self.pila_operandos)

    
    
# Generic Stack class for Poper & PSaltos
class Pila:
    def __init__(self, name):
        self.name = name
        self.stack = []  # Stack to store elements

    def push(self, element):
        """
        Method to add an element to the stack.
        """
        self.stack.append(element)
        print(f"Added {self.name}: {element}")

    def pop(self):
        """
        Method to remove the last element from the stack.
        """
        if not self.is_empty():
            element = self.stack.pop()
            print(f"Removed {self.name}: {element}")
            return element
        else:
            print(f"The {self.name} stack is empty")
            return None

    def top(self):
        """
        Method to get the last element without removing it from the stack.
        """
        if not self.is_empty():
            element = self.stack[-1]
            return element
        else:
            print(f"The {self.name} stack is empty")
            return None

    def is_empty(self):
        """
        Method to check if the stack is empty.
        """
        return len(self.stack) == 0

    def size(self):
        """
        Method to get the size of the stack.
        """
        return len(self.stack)



# Table of Quadruples class
class Quadruples:
    def __init__(self):
        # Initialize the table as a list of dictionaries
        self.table = []
        self.result_counter = 1  # Counter for result naming

    def add_entry(self, action, left_side=None, right_side=None, result=None):
        """
        Method to add an entry to the quadruples table. The result field is automatically generated if its not none.
        """
        if(result == None):
            result = f"t{self.result_counter}"
            self.result_counter += 1
        entry = {
            'action': action,
            'left_side': left_side,
            'right_side': right_side,
            'result': result
        }
        self.table.append(entry)
        print(f"Added entry: {entry}")

    def get_entry(self, index):
        """
        Method to get an entry by index from the quadruples table.
        """
        if 0 <= index < len(self.table):
            return self.table[index]
        else:
            print("Index out of range")
            return None
        
    def get_last_result(self):
        """
        Method to get the result of the last entry in the quadruples table.
        """
        if self.table:
            return self.table[-1]['result']
        else:
            print("The quadruples table is empty")
            return None

    def update_result(self, index, new_result):
        """
        Method to update the result of a specific entry in the quadruples table.
        """
        if 0 <= index < len(self.table):
            self.table[index]['result'] = new_result
            print(f"Updated entry at index {index} with new result: {new_result}")
        else:
            print("Index out of range")

    def size(self):
        """
        Method to get the number of entries in the quadruples table.
        """
        return len(self.table)

    def display(self):
        """
        Method to display the entire quadruples table.
        """
        for index, entry in enumerate(self.table):
            print(f"{index}: {entry}")


    
# Definition of Semantic Cube
SEM = {
    '+': {
        'int': {
            'int': 'int',
            'float': 'float',
            'bool': 'error'  # Operations with bool are errors
        },
        'float': {
            'int': 'float',
            'float': 'float',
            'bool': 'error'  # Operations with bool are errors
        },
        'bool': {
            'int': 'error',
            'float': 'error',
            'bool': 'error'  # Operations with bool are errors
        }
    },
    '-': {
        'int': {
            'int': 'int',
            'float': 'float',
            'bool': 'error'  # Operations with bool are errors
        },
        'float': {
            'int': 'float',
            'float': 'float',
            'bool': 'error'  # Operations with bool are errors
        },
        'bool': {
            'int': 'error',
            'float': 'error',
            'bool': 'error'  # Operations with bool are errors
        }
    },
    '*': {
        'int': {
            'int': 'int',
            'float': 'float',
            'bool': 'error'  # Operations with bool are errors
        },
        'float': {
            'int': 'float',
            'float': 'float',
            'bool': 'error'  # Operations with bool are errors
        },
        'bool': {
            'int': 'error',
            'float': 'error',
            'bool': 'error'  # Operations with bool are errors
        }
    },
    '/': {
        'int': {
            'int': 'int',
            'float': 'float',
            'bool': 'error'  # Operations with bool are errors
        },
        'float': {
            'int': 'float',
            'float': 'float',
            'bool': 'error'  # Operations with bool are errors
        },
        'bool': {
            'int': 'error',
            'float': 'error',
            'bool': 'error'  # Operations with bool are errors
        }
    },
    '=': {
        'int': {
            'int': 'int',
            'float': 'error',  # Cannot assign float to int
            'bool': 'error'  # Cannot assign bool to int
        },
        'float': {
            'int': 'float', 
            'float': 'float',
            'bool': 'error'  # Cannot assign bool to float
        },
        'bool': {
            'int': 'error',  # Cannot assign int to bool
            'float': 'error',  # Cannot assign float to bool
            'bool': 'bool'
        }
    },
    '>': {
        'int': {
            'int': 'bool',
            'float': 'bool',
            'bool': 'error'  # Operations with bool are errors
        },
        'float': {
            'int': 'bool',
            'float': 'bool',
            'bool': 'error'  # Operations with bool are errors
        },
        'bool': {
            'int': 'error',  # Operations with bool are errors
            'float': 'error',  # Operations with bool are errors
            'bool': 'bool'
        }
    },
    '<': {
        'int': {
            'int': 'bool',
            'float': 'bool',
            'bool': 'error'  # Operations with bool are errors
        },
        'float': {
            'int': 'bool',
            'float': 'bool',
            'bool': 'error'  # Operations with bool are errors
        },
        'bool': {
            'int': 'error',  # Operations with bool are errors
            'float': 'error',  # Operations with bool are errors
            'bool': 'bool'
        }
    },
    '!=': {
        'int': {
            'int': 'bool',
            'float': 'bool',
            'bool': 'error'  # Operations with bool are errors
        },
        'float': {
            'int': 'bool',
            'float': 'bool',
            'bool': 'error'  # Operations with bool are errors
        },
        'bool': {
            'int': 'error',  # Operations with bool are errors
            'float': 'error',  # Operations with bool are errors
            'bool': 'bool'
        }
    }
}
