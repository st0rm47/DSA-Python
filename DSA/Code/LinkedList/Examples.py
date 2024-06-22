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
        values = [] 
        current = self.head
        #Traverse the list
        while current is not None:
            #Add the data to the list
            values.append(current.data)
            #Move to the next node
            current = current.next
        
        current = self.head
        #Traverse the list
        while current is not None:
            #Assign the last element to the current node
            current.data = values.pop()
            #Move to the next node
            current = current.next
        