class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size
        self.load_factor = 0.7
        
    def get_hash(self, key):
        return key % self.size
    
    def setitem(self, key):
        h = self.get_hash(key)
        self.table[h] = key
        current_lf = sum(1 for i in self.table if i) / self.size
        if current_lf >= self.load_factor:
            self.rehash()
        
    def rehash(self):
        self.size *= 2
        new_table = [None] * self.size
        for key in self.table:
            if key:
                h = self.get_hash(key)
                new_table[h] = key
        self.table = new_table

        
    def display(self):
        for hash_value, key in enumerate(self.table):
            print(f"{hash_value}: {key}")
            
hash = HashTable()
keys = [1,300,209,17,12,24,36]
for key in keys:
    hash.setitem(key)
hash.display()
