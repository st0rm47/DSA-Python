from Min_Heap import min_heap

class PriorityQueue(min_heap):
        
    def __init__(self):
        super().__init__()
    
    def insert(self, value, priority):
        super().insert((priority, value))
    
    def extract_min(self):
        return super().extract_min()
    
    def get_min(self):
        return super().get_min()
    
    def size(self):
        return super().size()
    
    def print_heap(self):
        super().print_heap()
    
    def delete(self, i):
        super().delete(i)
    
    def build_heap(self, arr):
        super().build_heap(arr)
        
    def change_priority(self, value, new_priority):
        for i in range(self.size()):
            if self.heap[i][1] == value:
                old_priority = self.heap[i][0]
                self.heap[i] = (new_priority, value)
                
                if new_priority < old_priority:
                    self.heapify_up(i)
                else:
                    self.heapify_down(i)
                return
                """
                - The change_priority function changes the priority of an element in the priority queue.
                - It searches for the element in the heap and updates its priority.
                - If the new priority is less than the old priority, it calls the heapify_up function to maintain the heap property.
                - If the new priority is greater than the old priority, it calls the heapify_down function to maintain the heap property.
                - The time complexity of the change priority operation is O(log n) where n is the number of elements in the heap.
                """
    
    
# create a priority queue
priority_queue = PriorityQueue()

# insert elements with priority
priority_queue.insert('A', 3)
priority_queue.insert('B', 2)
priority_queue.insert('C', 1)
priority_queue.insert('D', 4)
priority_queue.insert('E', 5)

# print the priority queue
priority_queue.print_heap()

# extract the minimum element
print(f"Extracted element: {priority_queue.extract_min()}")
priority_queue.print_heap()

# change the priority of an element
priority_queue.change_priority('D', 1)
priority_queue.print_heap()

