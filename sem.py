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

class MemoryManager:
    def __init__(self):
        # Lists for storing variable values
        self.global_ints = []
        self.global_floats = []
        self.temp_ints = []
        self.temp_floats = []
        self.temp_bools = []
        self.const_ints = []
        self.const_floats = []
        self.const_strings = []

        # Base addresses for each memory segment
        self.base_addresses = {
            'Gi': 1000,
            'Gf': 2000,
            'Ti': 3000,
            'Tf': 4000,
            'Tb': 5000,
            'Ci': 6000,
            'Cf': 7000,
            'Cs': 8000,
        }

    def allocate(self, segment, value):
        """
        Method to allocate memory for a variable in the specified segment
        and store its value. Returns the virtual address of the allocated memory.
        """
        base_address = self.base_addresses[segment]
        if segment == 'Gi':
            self.global_ints.append(value)
            return base_address + len(self.global_ints) - 1
        elif segment == 'Gf':
            self.global_floats.append(value)
            return base_address + len(self.global_floats) - 1
        elif segment == 'Ti':
            self.temp_ints.append(value)
            return base_address + len(self.temp_ints) - 1
        elif segment == 'Tf':
            self.temp_floats.append(value)
            return base_address + len(self.temp_floats) - 1
        elif segment == 'Tb':
            self.temp_bools.append(value)
            return base_address + len(self.temp_bools) - 1
        elif segment == 'Ci':
            self.const_ints.append(value)
            return base_address + len(self.const_ints) - 1
        elif segment == 'Cf':
            self.const_floats.append(value)
            return base_address + len(self.const_floats) - 1
        elif segment == 'Cs':
            self.const_strings.append(value[1:-1])
            return base_address + len(self.const_strings) - 1
        else:
            raise ValueError("Invalid memory segment")

    def get_value(self, address):
        """
        Method to retrieve the value stored at a given virtual address.
        """
        if 1000 <= address < 2000:
            return self.global_ints[address - 1000]
        elif 2000 <= address < 3000:
            return self.global_floats[address - 2000]
        elif 3000 <= address < 4000:
            return self.temp_ints[address - 3000]
        elif 4000 <= address < 5000:
            return self.temp_floats[address - 4000]
        elif 5000 <= address < 6000:
            return self.temp_bools[address - 5000]
        elif 6000 <= address < 7000:
            return self.const_ints[address - 6000]
        elif 7000 <= address < 8000:
            return self.const_floats[address - 7000]
        elif 8000 <= address < 9000:
            return self.const_strings[address - 8000]
        else:
            raise ValueError("Invalid memory address")
        
    def display_memory(self):
        """
        Method to display all memory segments.
        """
        print("Global Integers:", self.global_ints)
        print("Global Floats:", self.global_floats)
        print("Temporary Integers:", self.temp_ints)
        print("Temporary Floats:", self.temp_floats)
        print("Temporary Booleans:", self.temp_bools)
        print("Constant Integers:", self.const_ints)
        print("Constant Floats:", self.const_floats)
        print("Constant Strings:", self.const_strings)




# Creation of class to define the structure of D_Functions & D_Vars
class D_Functions:
    def __init__(self, memory_manager):
        self.functions = {}  # Dictionary to save all the functions
        self.current_function = None
        self.global_function = None  # Variable to store the global function name
        self.memory_manager = memory_manager

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
                # Determine the memory segment and default value
                if self.current_function == self.global_function:
                    if variable_type == 'int':
                        segment = 'Gi'
                        default_value = 0
                    elif variable_type == 'float':
                        segment = 'Gf'
                        default_value = 0.0
                    else:
                        raise ValueError("Invalid global variable type")
                else:
                    if variable_type == 'int':
                        segment = 'Ti'
                        default_value = 0
                    elif variable_type == 'float':
                        segment = 'Tf'
                        default_value = 0.0
                    elif variable_type == 'bool':
                        segment = 'Tb'
                        default_value = False
                    else:
                        raise ValueError("Invalid local variable type")
                
                # Allocate memory and get the address
                address = self.memory_manager.allocate(segment, default_value)
                
                # Save the variable's name and memory address
                self.functions[self.current_function]['variables'][variable_name] = address
        else:
            raise ValueError("No current function selected.")

    def get_variable_type(self, variable_name):
        """
        Method to get the type of a variable by first looking in the current function's scope,
        and if not found, looking in the global function's scope.
        """
        # Check in the current function
        if self.current_function and variable_name in self.functions[self.current_function]['variables']:
            address = self.functions[self.current_function]['variables'][variable_name]
        # Check in the global function
        elif self.global_function and variable_name in self.functions[self.global_function]['variables']:
            address = self.functions[self.global_function]['variables'][variable_name]
        else:
            raise ValueError("Variable not found")  # Variable not found in either scope

        # Determine the type based on the address range
        if 1000 <= address < 2000:
            return 'int'
        elif 2000 <= address < 3000:
            return 'float'
        elif 3000 <= address < 4000:
            return 'int'
        elif 4000 <= address < 5000:
            return 'float'
        elif 5000 <= address < 6000:
            return 'bool'
        else:
            raise ValueError("Invalid memory address")
        
    def get_variable_address(self, variable_name):
        """
        Method to get the memory address of a variable by first looking in the current function's scope,
        and if not found, looking in the global function's scope.
        """
        # Check in the current function
        if self.current_function and variable_name in self.functions[self.current_function]['variables']:
            return self.functions[self.current_function]['variables'][variable_name]
        # Check in the global function
        elif self.global_function and variable_name in self.functions[self.global_function]['variables']:
            return self.functions[self.global_function]['variables'][variable_name]
        else:
            raise ValueError("Variable not found: ",variable_name)  # Variable not found in either scope
        
        
        

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
        #print(f"Added operand: {operando} with type: {tipo}")

    def pop(self):
        """
        Method to remove the last operand and its type from the stacks.
        """
        if not self.is_empty():
            operando = self.pila_operandos.pop()
            tipo = self.pila_tipos.pop()
            #print(f"Removed operand: {operando} with type: {tipo}")
            return operando, tipo
        else:
            #print("The stacks are empty")
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
            #print("The stacks are empty")
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
        #print(f"Added {self.name}: {element}")

    def pop(self):
        """
        Method to remove the last element from the stack.
        """
        if not self.is_empty():
            element = self.stack.pop()
            #print(f"Removed {self.name}: {element}")
            return element
        else:
            #print(f"The {self.name} stack is empty")
            return None

    def top(self):
        """
        Method to get the last element without removing it from the stack.
        """
        if not self.is_empty():
            element = self.stack[-1]
            return element
        else:
            #print(f"The {self.name} stack is empty")
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
    def __init__(self, memory_manager):
        # Initialize the table as a list of dictionaries
        self.table = []
        self.memory_manager = memory_manager

    def add_entry(self, action, left_side=-1, right_side=-1,result=-1, result_type=-1):
        """
        Method to add an entry to the quadruples table. The result field is automatically generated based on the result type.
        """
        if result_type is not -1:
            if result_type == 'int':
                result = self.memory_manager.allocate('Ti', 0)
            elif result_type == 'float':
                result = self.memory_manager.allocate('Tf', 0.0)
            elif result_type == 'bool':
                result = self.memory_manager.allocate('Tb', False)
            else:
                raise ValueError("Unsupported result type")

        entry = {
            'action': action,
            'left_side': left_side,
            'right_side': right_side,
            'result': result
        }
        self.table.append(entry)
        #print(f"Added entry: {entry}")

    def get_entry(self, index):
        """
        Method to get an entry by index from the quadruples table.
        """
        if 0 <= index < len(self.table):
            return self.table[index]
        else:
            #print("Index out of range")
            return -1
        
    def get_last_result(self):
        """
        Method to get the result of the last entry in the quadruples table.
        """
        if self.table:
            return self.table[-1]['result']
        else:
            print("The quadruples table is empty")
            return -1

    def update_result(self, index, new_result):
        """
        Method to update the result of a specific entry in the quadruples table.
        """
        if 0 <= index < len(self.table):
            self.table[index]['result'] = new_result
            #print(f"Updated entry at index {index} with new result: {new_result}")
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
    operation_codes['+']: {
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
    operation_codes['-']: {
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
    operation_codes['*']: {
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
    operation_codes['/']: {
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
    operation_codes['=']: {
        'int': {
            'int': 'int',
            'float': 'error',  # Cannot assign float to int
            'bool': 'error'  # Cannot assign bool to int
        },
        'float': {
            'int': 'error', # Cannot assign int to float
            'float': 'float',
            'bool': 'error'  # Cannot assign bool to float
        },
        'bool': {
            'int': 'error',  # Cannot assign int to bool
            'float': 'error',  # Cannot assign float to bool
            'bool': 'bool'
        }
    },
    operation_codes['>']: {
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
    operation_codes['<']: {
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
    operation_codes['!=']: {
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
