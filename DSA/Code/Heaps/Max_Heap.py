class max_heap:
    def __init__(self):
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
    
    #swaps the elements at indices i and j
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    #inserts a key into the heap  
    def insert(self, key):
        #insert the key at the end of the heap
        self.heap.append(key)

        self.heapify_up(self.size() - 1)
    
    # maintains the heap property by comparing the key with its parent and swapping them if the key is larger than the parent
    def heapify_up(self, i):
        parent = self.parent(i)
        while i != 0 and self.heap[parent] < self.heap[i]:
            self.swap(i, parent)
            i = parent
    
        """
        - The insert here adds the key to the end of the heap and then calls the heapify_up function to maintain the heap property.
        - The heapify_up function compares the key with its parent and swaps them if the key is larger than the parent.
        - The function continues to compare the key with its parent until the heap property is satisfied.
        - The time complexity of the insert operation is O(log n) where n is the number of elements in the heap.
        """
    
    # extracts the maximum element from the heap
    def extract_max(self):
        if self.size() == 0:
            return None
        if self.size() == 1:
            return self.heap.pop()
        
        # The root of the heap is the maximum element 
        root = self.heap[0]
        # Replace the root with the last element of the heap
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root
    
    # maintains the heap property by comparing the key with its children and swapping it with the largest child if the key is smaller than the child
    def heapify_down(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        largest = i
        if left < self.size() and self.heap[left] > self.heap[largest]:
            largest = left
        if right < self.size() and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.swap(i, largest)
            self.heapify_down(largest)
            
        """
        - The extract_max function removes the maximum element from the heap and returns it.
        - The root of the heap is the maximum element, so we remove it and replace it with the last element of the heap.
        - We then call the heapify_down function to maintain the heap property.
        - The heapify_down function compares the key with its children and swaps it with the largest child if the key is smaller than the child.
        - The function continues to compare the key with its children until the heap property is satisfied.
        - The time complexity of the extract_max operation is O(log n) where n is the number of elements in the heap.
        """

    # builds a heap from an array of elements
    def build_heap(self, arr):
        self.heap = arr
        for i in range(self.size()//2, -1, -1):
            self.heapify_down(i)
    
    def peek (self):
        if self.size() == 0:
            return None
        return self.heap[0]
    
    def print_heap(self):
        print(self.heap)
        
        
max = max_heap()
max.insert(1)
max.insert(2)
max.insert(3)
max.insert(4)
max.insert(5)
max.insert(6)
max.insert(7)
max.insert(8)
max.insert(9)
print(f"The Max Heap is: {max.heap}")
max.print_heap()
print(f"The Max val is: {max.extract_max()}")
max.print_heap()
max.build_heap([9, 4, 7, 1, -2, 6, 5])
max.print_heap()
print(f"The Max val is: {max.extract_max()}")
max.print_heap()


        
        