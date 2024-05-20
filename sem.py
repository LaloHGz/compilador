
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

    def peek(self):
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

    
# Stack Poper class
class Poper:
    def __init__(self):
        self.pila_operadores = []  # Stack to store operators

    def push(self, operador):
        """
        Method to add an operator  to the stack.
        """
        self.pila_operadores.append(operador)
        print(f"Added operator: {operador}")

    def pop(self):
        """
        Method to remove the last operator from the stack.
        """
        if not self.is_empty():
            operador = self.pila_operadores.pop()
            print(f"Removed operator: {operador}")
            return operador
        else:
            print("The stack is empty")
            return None

    def peek(self):
        """
        Method to get the last operator without removing it from the stack.
        """
        if not self.is_empty():
            operador = self.pila_operadores[-1]
            return operador
        else:
            print("The stack is empty")
            return None

    def is_empty(self):
        """
        Method to check if the stack is empty.
        """
        return len(self.pila_operadores) == 0

    def size(self):
        """
        Method to get the size of the stack.
        """
        return len(self.pila_operadores)
    
    
class Quadruples:
    def __init__(self):
        # Initialize the table as a list of dictionaries
        self.table = []

    def add_entry(self, action, left_side=None, right_side=None, result=None):
        """
        Method to add an entry to the quadruples table.
        """
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
            'float': 'float'
        },
        'float': {
            'int': 'float',
            'float': 'float'
        }
    },
    '-': {
        'int': {
            'int': 'int',
            'float': 'float'
        },
        'float': {
            'int': 'float',
            'float': 'float'
        }
    },
    '*': {
        'int': {
            'int': 'int',
            'float': 'float'
        },
        'float': {
            'int': 'float',
            'float': 'float'
        }
    },
    '/': {
        'int': {
            'int': 'int',
            'float': 'float'
        },
        'float': {
            'int': 'float',
            'float': 'float'
        }
    },
    '=': {
        'int': {
            'int': 'int',
            'float': 'error'  # Cannot assign float to int
        },
        'float': {
            'int': 'float', 
            'float': 'float'
        }
    },
    '>': {
        'int': {
            'int': 'bool',
            'float': 'bool'
        },
        'float': {
            'int': 'bool',
            'float': 'bool'
        }
    },
    '<': {
        'int': {
            'int': 'bool',
            'float': 'bool'
        },
        'float': {
            'int': 'bool',
            'float': 'bool'
        }
    },
    '!=': {
        'int': {
            'int': 'bool',
            'float': 'bool'
        },
        'float': {
            'int': 'bool',
            'float': 'bool'
        }
    }
}

