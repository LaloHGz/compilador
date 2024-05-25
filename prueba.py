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
            self.const_strings.append(value)
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

# Ejemplo de uso del MemoryManager
memory_manager = MemoryManager()

# Asignar valores a diferentes segmentos de memoria
memory_manager.allocate('Gi',22)
memory_manager.allocate('Gi', "A")
print(memory_manager.get_value(1000))
print(memory_manager.get_value(1001))