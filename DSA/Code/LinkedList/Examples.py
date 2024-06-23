#Largest Number in a linked list
def largestNode(self):
    if self.head is None:
        return "List is empty"
    else:
        current = self.head
        #Assume the first node is the largest
        max = current.data
        #Traverse the list
        while current is not None:
            #If current node's data is greater than max
            if current.data > max:
                #Update max
                max = current.data
            #Move to the next node
            current = current.next
        #Return the largest number
        return max
    

#Linked List is Sorted or Not
def isSorted(self):
    if self.head is None:
        return "List is empty"
    else:
        current = self.head
        #Traverse the list
        while current.next is not None:
            #If current node's data is greater than next node's data
            if current.data > current.next.data:
                return "List is not sorted"
            #Move to the next node
            current = current.next
        #If the loop completes, the list is sorted
        return "List is sorted"

#Remove Duplicates from a sorted linked list
def removeDuplicates(self):
    if self.head is None:
        return "List is empty"
    else:
        current = self.head
        #Traverse the list
        while current.next is not None:
            #If current node's data is equal to next node's data
            if current.data == current.next.data:
                #Remove the next node
                current.next = current.next.next
            else:
                #Move to the next node
                current = current.next
        #Return the list without duplicates
        return self

#Reverse a linked list
def reverse(self):
    if self.head is None:
        return "List is empty"
    else:
        prev_node = None
        current = self.head
        #Traverse the list
        while current is not None:
            #Store the next node
            next_node = current.next
            #Reverse the link
            current.next = prev_node
            #Move pointers one position ahead
            prev_node = current
            current = next_node
        #Update the head
        self.head = prev_node
        #Return the reversed list
        return self
    

#Merge two sorted linked lists
def concatenate(self,list2):
    if self.head is None:
        return "List1 is empty"
    elif list2.head is None:
        return "List2 is empty"
    else:
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = list2.head
        return self
    

#Middle element of a linked list
def middleElement(self):
    if self.head is None:
        return "List is empty"
    else:
        slow_ptr = self.head
        fast_ptr = self.head
        #Traverse the list
        while fast_ptr is not None and fast_ptr.next is not None:
            #Move slow_ptr one position ahead
            slow_ptr = slow_ptr.next
            #Move fast_ptr two positions ahead
            fast_ptr = fast_ptr.next.next
        #Return the middle element
        return slow_ptr.data