from dataclasses import dataclass

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

