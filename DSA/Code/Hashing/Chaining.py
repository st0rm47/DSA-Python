class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        current = self.head
        if current is None:
            self.head = Node(data)
        else:
            while current.next:
                current = current.next
            current.next = Node(data)
            
    def traverse(self):
        current = self.head
        result = ''
        while current:
            result += (f"{current.data}->")
            current = current.next
        result+= "None"
        print(result)
        
class HashData:
    def __init__(self):
        self.table = [None] * 10
        
    def get_hash(self, key):
        return key % 10
    
    def setitem(self, key):
        #insert key into the hash table
        h = self.get_hash(key)
        #check if the hash table is empty
        if self.table[h] is None:
            #create a new linked list and insert the key
            self.table[h] = Linkedlist()
            #insert the key into the linked list
            self.table[h].insert(key)
        else:
            self.table[h].insert(key)

    def display(self):
        for hash_value, key in enumerate(self.table):
            if key is not None:
                print(f"{hash_value}:", end=" ")
                key.traverse()
            else:
                print(f"{hash_value}: None")
    
    def getitem(self, key):
        h = self.get_hash(key)
        if self.table[h] is not None:
            current = self.table[h].head
            while current:
                if current.data == key:
                    return {"hash_value": h, "key": key}
                current = current.next
            return "Key not found"
        else:
            return "Key not found"

keys = [12, 17, 15, 4, 27, 14, 37]
hash = HashData()

for key in keys:
    hash.setitem(key)
hash.display()
print(hash.getitem(15))
print(hash.getitem(14))
print(hash.getitem(37))
print(hash.getitem(100))

    