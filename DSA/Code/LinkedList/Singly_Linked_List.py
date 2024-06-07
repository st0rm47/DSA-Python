#Singly Linked List

# create the Node class
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# create the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
    
    # method to create a linked list
    def create_linked_list(self):
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
        node2.next = node3
        node3.next = node4
        node4.next = None

    # method to traverse and print the nodes
    def traverse_linked_list(self):
        current = self.head
        while current is not None:
            print(f"{current.data}", end="->")
            current = current.next

linked_list = LinkedList()
# create a linked list
linked_list.create_linked_list()
# print the linked list
linked_list.traverse_linked_list()