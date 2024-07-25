#Stack

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def peek(self):
        if len(self.stack) < 1:
            return None
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def display(self):
        return self.stack
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.display())
print("Popped:", stack.pop())
print("Peek:", stack.peek())
print("Size:", stack.size())
print("Is empty:", stack.is_empty())
print("Stack:", stack.display())
