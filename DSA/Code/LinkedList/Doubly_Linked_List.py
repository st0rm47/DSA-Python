# Doubly Linked List

# create the Node class
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

# create the DoublyLinkedList class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    # method to create a doubly linked list
    def create_doubly_linked_list(self):
        # take input for node data
        data1 = int(input())
        data2 = int(input())
        data3 = int(input())
        data4 = int(input())
        # create 4 nodes with input values
        node1 = Node(data1)
        node2 = Node(data2)
        node3 = Node(data3)
        node4 = Node(data4)
        # set head field to the first node
        self.head = node1
        # link the nodes
        node1.next = node2
        node2.prev = node1
        node2.next = node3
        node3.prev = node2
        node3.next = node4
        node4.prev = node3
        node4.next = None

    # method to traverse and print the nodes
    def traverse_doubly_linked_list(self):
        current = self.head
        while current is not None:
            print(f"{current.data}", end="->")
            current = current.next
            
linked_list = DoublyLinkedList()
# create a doubly linked list
linked_list.create_doubly_linked_list()
# print the doubly linked list
linked_list.traverse_doubly_linked_list()
