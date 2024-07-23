#Maximum in a Circular Linked List
def maxNode(self):
    if self.head is None:
        return "List is empty"
    else:
        current = self.head
        #Set the maximum to the first node
        max = current.data
        #Traverse the list
        while current.next is not self.head:
            #Update the maximum
            if current.data > max:
                max = current.data
            #Move to the next node
            current = current.next
        return max

#Reverse a Circular Linked List
def reverse(self):
    if self.head is None:
        return "List is empty"
    else:
        prev_node = None
        current = self.head
        next_node = current.next
        #Traverse the list
        while True:
            #Change the next of the current node to the previous node
            current.next = prev_node
            #Move the pointers one position ahead
            prev_node = current
            current = next_node
            next_node = current.next
            #Stop when the last node is reached
            if current is self.head:
                break
        
        #Set the head to the last node
        self.head.next = prev_node
        return self

#Searching in a Circular Linked List
def search(self, value):
    if self.head is None:
        return "List is empty"
    else:
        current = self.head
        #Traverse the list
        while True:
            #Check if the value is found
            if current.data == value:
                return "Value found"
            #Move to the next node
            current = current.next
            #Stop when the last node is reached
            if current is self.head:
                break
        return "Value not found"