# Delete the first node of the linked list
def delete_first_node(self):
    # set the head to the next node
    self.head = self.head.next
    return

# Delete the node at given position
def delete_node_at_position(self, position):
    current = self.head
    # Traverse to the node before the position
    for i in range(position - 2):
        # If the next node is the node to be deleted
        current = current.next
    # Set the next node to the next of the next node
    current.next = current.next.next
    
# Delete the last node of the linked list
def delete_last_node(self):
    current = self.head
    # Traverse to the second last node
    for i in range(self.size - 2):
        # If the next node is the last node
        current = current.next
    # Set the next node to None    
    current.next = None