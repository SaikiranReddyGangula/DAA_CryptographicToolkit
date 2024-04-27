class CuckooHashTable:
    def __init__(self, size):
        self.size = size
        self.table1 = [None] * size
        self.table2 = [None] * size
        self.max_attempts = 5

    def hash_function1(self, key):
        return hash(key)

    def hash_function2(self, key):
        # Add some manipulation to the key before hashing
        return hash(key + "salt")  # Example manipulation

    def insert(self, key, value):
        for _ in range(self.max_attempts):
            index1 = self.hash_function1(key) % self.size
            index2 = self.hash_function2(key) % self.size

            if self.table1[index1] is None:
                self.table1[index1] = (key, value)
                return True
            elif self.table2[index2] is None:
                self.table2[index2] = (key, value)
                return True
            else:
                displaced_key, displaced_value = self.table1[index1]
                self.table1[index1] = (key, value)
                key, value = displaced_key, displaced_value
                self.table2[index2] = (key, value)

        # If maximum attempts reached, trigger rehashing
        self.rehash()

    def lookup(self, key):
        index1 = self.hash_function1(key) % self.size
        index2 = self.hash_function2(key) % self.size

        if self.table1[index1] and self.table1[index1][0] == key:
            return self.table1[index1][1]
        elif self.table2[index2] and self.table2[index2][0] == key:
            return self.table2[index2][1]
        else:
            return None

    def delete(self, key):
        index1 = self.hash_function1(key) % self.size
        index2 = self.hash_function2(key) % self.size

        if self.table1[index1] and self.table1[index1][0] == key:
            self.table1[index1] = None
            return True
        elif self.table2[index2] and self.table2[index2][0] == key:
            self.table2[index2] = None
            return True
        else:
            return False

    def rehash(self):
        # Implement rehashing logic
        pass
