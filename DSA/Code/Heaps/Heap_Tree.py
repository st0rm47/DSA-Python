class Heap_Tree:
    def __init__ (self):
        self.heap = []
    
    #returns the number of elements in the heap  
    def size (self):
        return len(self.heap)
    
    #returns the index of the parent node
    def parent(self, i):
        return (i-1)//2
    
    #returns the index of the left child
    def left_child(self, i):
        return 2*i + 1
    
    #returns the index of the right child
    def right_child(self, i):
        return 2*i + 2

    def print_heap(self):
        print(self.heap)
    
heap = Heap_Tree()
heap.heap = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"The size of the heap is {heap.size()}")
print(f"The parent of 2 is {heap.parent(2)}")
print(f"The left child of 2 is {heap.left_child(2)}")
print(f"The right child of 2 is {heap.right_child(2)}")
heap.print_heap()

    

