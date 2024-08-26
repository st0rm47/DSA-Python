class HashData:
    def __init__(self):
        self.table = [None] * 15
    
    def hash(self, key):
        return key % 15
    
    def insert(self, key):
        i = 0
        h = self.hash(key)
        while self.table[h] is not None:
            # increment i for linear probing
            i += 1
            # recalculate hash value
            h = (h + i) % 15
        # insert key at calculated hash value
        self.table[h] = key
    
    def display(self):
        for hash_value, key in enumerate(self.table):
            print(f"{hash_value}: {key}")
            
    def get(self, key):
        i = 0
        h = self.hash(key)
        while self.table[h] is not None:
            if self.table[h] == key:
                return h
            i += 1
            h = (h + i) % 15
        return None
            
keys = [10, 22, 31, 4, 15, 28, 17, 88, 59]
hash1 = HashData()
for key in keys:
    hash1.insert(key)
hash1.display()
print(hash1.get(15))
print(hash1.get(17))
print(hash1.get(88))
