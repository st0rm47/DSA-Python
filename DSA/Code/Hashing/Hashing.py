class HashData:
    def __init__(self):
        self.table = [None] * 10
        
    def get_hash(self, key):
        return key % 10
    
    def setitem(self, key):
        h = self.get_hash(key)
        self.table[h] = key
        
    def getitem(self, key):
        h = self.get_hash(key)
        key  = self.table[h]
        return {"hash_value": h, "key": key}
    
    def display(self):
        for hash_value, key in enumerate(self.table):
            print(f"{hash_value}: {key}")
                
keys = [1,300,209,117,12]
hash = HashData()
for key in keys:
    hash.setitem(key)
hash.display()
print(hash.getitem(209))
