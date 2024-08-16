class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):
        if self.isFull():
            print("Queue is Full")
        elif self.front == -1:  # Queue is empty
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        temp = self.queue[self.front]
        if self.front == self.rear:  # Only one element was present
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return temp

    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            i = self.front
            while i != self.rear:
                print(self.queue[i], end=" ")
                i = (i + 1) % self.size
            print(self.queue[i])

    def getFront(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        return self.queue[self.front]
    
    def getRear(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        return self.queue[self.rear]
    
    def isEmpty(self):
        return self.front == -1
    
    def isFull(self):
        return (self.rear + 1) % self.size == self.front
    

cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.display()
print("Dequeued:", cq.dequeue())
print("Dequeued:", cq.dequeue())
print("Dequeued:", cq.dequeue())
print("Dequeued:", cq.dequeue())
print("Dequeued:", cq.dequeue())
cq.display()
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.display()
print("Front element:", cq.getFront())
print("Rear element:", cq.getRear())
print("Queue empty:", cq.isEmpty())
print("Queue full: ", cq.isFull())
