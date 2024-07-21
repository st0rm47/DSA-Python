#Deletiom of first node in circular linked list
def delete_first_node(self):
    # If the list is empty
    if self.head is None:
        return "The list has no element to delete"
    
    temp = self.head
    current = self.head
    # Traverse to the last node
    while current.next != self.head:
        current = current.next
    # Set the next of the last node to the next of the head
    self.head = temp.next
    # Set the next of the last node to the new head
    current.next = self.head
    
# Deletion of the last node in the circular linked list
def delete_last_node(self):
    # Set the next of the second last node to the head
    current = self.head
    while current.next.next != self.head:
        current = current.next
    current.next = self.head
    
# Deletion of the node at a given position in the circular linked list
def delete_node_at_position(self, position):
    # Get the node at the given position
    current = self.head
    prev_node = None
    for i in range(position - 1):
        prev_node = current
        current = current.next
    # Set the next of the previous node to the next of the current node
    prev_node.next = current.next
    