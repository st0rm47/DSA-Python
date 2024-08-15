#Queue

class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    
    def display(self):
        print(self.queue)
        
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def peek(self):
        if len(self.queue) < 1:
            return None
        return self.queue[0]

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()
print("Dequeued:", queue.dequeue())
print("Peek:", queue.peek())
print("Size:", queue.size())
print("Is empty:", queue.isEmpty())
queue.display()
