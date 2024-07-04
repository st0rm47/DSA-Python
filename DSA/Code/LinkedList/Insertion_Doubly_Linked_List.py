#create Node Class
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

#Insertion at the End of the Linked List
def insert_at_end(self,data):
    # create a new node
    new_node = Node(data)
    # set current to head
    current = self.head
    # traverse to the last node
    while current.next is not None:
        # move to the next node
        current = current.next
    # link the new node to the last node
    current.next = new_node
    new_node.prev = current

#Insertion at the Beginning of the Linked List
def insert_at_beginning(self,data):
    # create a new node
    new_node = Node(data)
    # link the new node to the head
    new_node.next = self.head
    # set the head to the new node
    self.head = new_node
    new_node.prev = None

#Insertion at the Given Position of the Linked List
def insert_at_position(self,data,position):
    # create a new node
    new_node = Node(data)
    # set current to head
    current = self.head
    for i in range(position-2):
        # move to the next node
        current = current.next
    # link the new node to the next node
    new_node.next = current.next
    new_node.prev = current
    # link the new node to the current node
    current.next = new_node
    current.next.prev = new_node