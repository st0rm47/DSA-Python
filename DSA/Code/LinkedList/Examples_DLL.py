#Reverse a Doubly Linked List
def  reverse(self):
    if self.head is None:
        return "List is empty"
    else:
        current = self.head
        #Traverse the list
        while current is not None:
            # Save the previous node
            temp = current.prev
            # Change the previous node to the next node
            current.prev = current.next
            current.next = temp
            # Move to the next node
            current = current.prev
            
        # Set the head to the last node
        if temp is not None:
            self.head = temp.prev
        return self

#Check if a linked list is a palindrome
def isPalindrome(self):
    if self.head is None:
        return "List is empty"
    else:
        #Create an empty list
        lst = []
        current = self.head
        #Traverse the list
        while current is not None:
            #Append the data of each node to the list
            lst.append(current.data)
            #Move to the next node
            current = current.next
        #Check if the list is equal to its reverse
        if lst == lst[::-1]:
            return "List is a palindrome"
        else:
            return "List is not a palindrome"