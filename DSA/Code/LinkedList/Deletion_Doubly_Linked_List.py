# Deletion the first node of the doubly linked list
def delete_first_node(self):
    # Set the head to the next node
    self.head = self.head.next
    # Set the previous of the new head to None
    self.head.prev = None
    return

# Deletion the last node of the doubly linked list
def delete_last_node(self):
    # Set the tail to the previous node
    self.tail = self.tail.prev
    # Set the next of the new tail to None
    self.tail.next = None

# Deletion the node at a given position of the doubly linked list
def delete_node_at_position(self, position):
    # Get the node at the given position
    current = self.head
    for i in range(position):
        current = current.next
    # Set the next of the previous node to the next of the current node
    current.prev.next = current.next
    # Set the previous of the next node to the previous of the current node
    current.next.prev = current.prev
    return