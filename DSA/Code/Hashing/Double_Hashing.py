class HashData:
    def __init__(self):
        self.table = [None] * 10
    
    def hash(self, key, i= 0):
        return (self.primary_hash(key) + i * self.secondary_hash(key)) % 10
    
    def primary_hash(self, key):
        return key % 10
    
    def secondary_hash(self, key):
        return 1 + (key % 9)
    
    def insert(self, key):
        i = 0
        h = self.hash(key)
        while self.table[h] is not None:
            # increment i for double hashing
            i += 1
            # recalculate hash value
            h = self.hash(key,i)
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
            h = self.hash(key,i)
        return None
            
keys = [12, 17, 15, 4, 27, 14, 37]
hash1 = HashData()
for key in keys:
    hash1.insert(key)
hash1.display()
print(hash1.get(15))
print(hash1.get(17))
print(hash1.get(88))
