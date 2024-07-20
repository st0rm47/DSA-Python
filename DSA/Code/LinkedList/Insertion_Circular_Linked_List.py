#Create Node CLass
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

#Insert at the End of the Circular Linked List
def insert_at_end(self,data):
    # create a new node
    new_node = Node(data)
    # set current to head
    current = self.head
    # traverse to the last node
    while current.next is not self.head:
        # move to the next node
        current = current.next
    # link the new node to the last node
    current.next = new_node
    new_node.next = self.head

#Insert at the Beginning of the Circular Linked List
def insert_at_beginning(self,data):
    # create a new node
    new_node = Node(data)
    # set current to head
    current = self.head
    # traverse to the last node
    while current.next is not self.head:
        # move to the next node
        current = current.next
    # link the new node to the last node
    current.next = new_node
    new_node.next = self.head
    # update the head to the new node
    self.head = new_node
    
#Insert at the Given Position of the Circular Linked List
def insert_at_position(self,data,position):
    # create a new node
    new_node = Node(data)
    # set current to head
    current = self.head
    # traverse to the position
    for i in range(position-1):
        # move to the next node
        current = current.next
    # link the new node to the next node
    new_node.next = current.next
    current.next = new_node
