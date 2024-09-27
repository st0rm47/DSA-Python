# *Data Structures and Algorithms*

- Data structures and algorithms (DSA) are fundamental concepts in computer science that enable efficient problem-solving. 
- Data structures are ways of organizing and storing data so that it can be accessed and modified efficiently. 
- Algorithms are step-by-step procedures for solving problems and performing computations.

    ## *Data Structures*
    - Data structures are used to store and organize data in a computer so that it can be used efficiently.
    - Some common data structures include arrays, linked lists, stacks, queues, trees, and graphs.

    ## *Algorithms*
    - Algorithms are step-by-step procedures for solving problems and performing computations.
    - Some common algorithms include sorting algorithms, searching algorithms, and graph algorithms.
***

# *Python Lists*
- Python lists are a type of data structure that can store multiple elements.
- Lists are mutable, which means that their elements can be changed after they are created.

    <details> 
    <summary> List  Slicing </summary>

    ## *List Slicing*
    - List slicing is a way to access a subset of elements from a list.
    - List slicing uses the syntax `list[start:end:step]` to specify the start index, end index, and step size.
    - ```python
        list = [1, 2, 3, 4, 5]
        print(list[1:4]) # Output: [2, 3, 4]
      ```
    ***
    </details>

    <details> 
    <summary> List Method </summary>

    ## *List Method*
    - Python lists have many built-in methods that can be used to modify and manipulate lists.
    - Some common list methods include `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `index()`, `count()`, `sort()`, and `reverse()`.

      ### *List Append*
      - The `append()` method adds an element to the end of a list.
      - ```python
          list = [1, 2, 3]
          list.append(4)
          print(list) # Output: [1, 2, 3, 4]
        ```
    
      ### *List Extend*
      - The `extend()` method adds the elements of one list to the end of another list.
      - ```python
          list1 = [1, 2, 3]
          list2 = [4, 5, 6]
          list1.extend(list2)
          print(list1) # Output: [1, 2, 3, 4, 5, 6]
        ```
      
      ### *List Pop*
      - The `pop()` method removes and returns the element at a specified index.
      - ```python
          list = [1, 2, 3, 4]
          element = list.pop(2)
          print(element) # Output: 3
          print(list) # Output: [1, 2, 4]
        ```
      
      ### *List Insert*
      - The `insert()` method inserts an element at a specified index.
      - ```python
          list = [1, 2, 3, 4]
          list.insert(2, 5)
          print(list) # Output: [1, 2, 5, 3, 4]
        ```
      
      ### *List Remove*
      - The `remove()` method removes the first occurrence of a specified element from a list.
      - ```python
          list = [1, 2, 3, 4, 3]
          list.remove(3)
          print(list) # Output: [1, 2, 4, 3]
        ```
      
      ### *List Index*
      - The `index()` method returns the index of the first occurrence of a specified element in a list.
      - ```python
          list = [1, 2, 3, 4]
          index = list.index(3)
          print(index) # Output: 2
        ```

      ### *List Count*
      - The `count()` method returns the number of occurrences of a specified element in a list.
      - ```python
          list = [1, 2, 3, 4, 3]
          count = list.count(3)
          print(count) # Output: 2
        ```
      
      ### *List Sort*
      - The `sort()` method sorts the elements of a list in ascending order.
      - ```python
          list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
          list.sort()
          print(list) # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]
        ```
      
      ### *List Reverse*
      - The `reverse()` method reverses the order of the elements in a list.
      - ```python
          list = [1, 2, 3, 4]
          list.reverse()
          print(list) # Output: [4, 3, 2, 1]
        ```
***
</details>

# *Sorting*

- Sorting is the process of arranging elements in a list in a specific order.
- There are many different sorting algorithms that can be used to sort a list of elements.

  <details>
  <summary> Bubble Sort </summary>
  
  ## *Bubble Sort*
  - Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
  - The algorithm continues to pass through the list until no swaps are needed, indicating that the list is sorted.
  - Bubble sort has a time complexity of O(n^2) in the worst case.
  - Bubble sort space complexity is O(1).
  - Bubble sort is not a practical sorting algorithm for large lists.
  - *[Code](Code/Sorting/Bubble_Sort.py)*
  ![alt text](images/Bubble_Sort.png)
  ![alt text](images/Bubble_Sort2.png)
  ***
  </details>
  
  <details>
  <summary> Selection Sort </summary>

  ## *Selection Sort*
  - Selection sort is a simple sorting algorithm that repeatedly selects the minimum element from an unsorted portion of the list and swaps it with the first unsorted element.
  - The algorithm divides the list into a sorted and an unsorted portion, with the sorted portion growing from left to right.
  - Selection sort has a time complexity of O(n^2) in the worst case.
  - Selection sort space complexity is O(1).
  - Selection sort is not a practical sorting algorithm for large lists.
  - *[Code](Code/Sorting/Selection_Sort.py)*
  ![alt text](images/Selection_Sort.png)
  ![alt text](images/Selection_Sort2.png)
  ***
  </details>
  
  <details>
  <summary> Insertion Sort </summary>

  ## *Insertion Sort*
  - Insertion sort is a simple sorting algorithm that works by building a sorted list one element at a time.
  - The algorithm iterates over the list, removing one element at a time and inserting it into its correct position in the sorted portion of the list.
  - Insertion sort has a time complexity of O(n^2) in the worst case.
  - Insertion sort space complexity is O(1).
  - Insertion sort is efficient for small lists or nearly sorted lists.
  - *[Code](Code/Sorting/Insertion_Sort.py)*
  ![alt text](images/Insertion_Sort.png)
  ![alt text](images/Insertion_Sort2.png)
  ***
  </details>

  <details>
  <summary> Merge Sort </summary>

  ## *Merge Sort*
  - Merge sort is a divide-and-conquer sorting algorithm that recursively divides the list into smaller sublists, sorts the sublists, and then merges them back together.
  - The algorithm uses a "merge" operation to combine two sorted sublists into a single sorted list.
  - Merge sort has a time complexity of O(n log n) in the worst case.
  - Merge sort space complexity is O(n).
  - Merge sort is a stable sorting algorithm that is efficient for large lists.
  - *[Code](Code/Sorting/Merge_Sort.py)*
  ![alt text](images/Merge_Sort.png)
  ![alt text](images/Merge_Sort2.png)
  ![alt text](images/Merge_Sort3.png)
  ![alt text](images/Merge_Sort4.png)
  - ***Working of  Code***
  ![alt text](images/Merge_Sort5.png)
  ***
  </details>

  <details>
  <summary> Quick Sort </summary>

  ## *Quick Sort*
  - Quick sort is a divide-and-conquer sorting algorithm that recursively divides the list into smaller sublists, sorts the sublists, and then combines them back together.
  - The algorithm uses a "pivot" element to partition the list into two sublists, with elements less than the pivot on one side and elements greater than the pivot on the other side.
  - Quick sort has a time complexity of O(n log n) in the average case and O(n^2) in the worst case.
  - Quick sort space complexity is O(log n).
  - Quick sort is an efficient sorting algorithm that deals with diverse data.
  - *[Code](Code/Sorting/Quick_Sort.py)*
  ![alt text](images/Quick_Sort.png)
  ![alt text](images/Quick_Sort2.png)
  ![alt text](images/Quick_Sort3.png)
  ![alt text](images/Quick_Sort4.png)
  ***
  </details>

  <details>
  <summary> Counting Sort </summary>

  ## *Counting Sort*
  - Counting sort is a non-comparison-based sorting algorithm that works by counting the number of occurrences of each element in the list.
  - The algorithm then uses this information to construct a sorted list.
  - Counting sort has a time complexity of O(n + k) in the best and average cases and O(n + k) in the worst case, where k is the range of the input.
  - Counting sort space complexity is O(n + k).
  - Counting sort is efficient for sorting lists with a small range of integers and non-negative values.
  - *[Code](Code/Sorting/Counting_Sort.py)*
  ![alt text](images/Counting_Sort.png)
  ![alt text](images/Counting_Sort2.png)
  ![alt text](images/Counting_Sort3.png)
  ***
  </details>
***
</details>

# *Searching*

- Searching is the process of finding a specific element in a list.
- There are many different searching algorithms that can be used to search for an element in a list.

  <details>
  <summary> Linear Search </summary>

  ## *Linear Search*
  - Linear search is a simple searching algorithm that sequentially checks each element in a list until the target element is found.
  - The algorithm has a time complexity of O(n) in the worst case, where n is the number of elements in the list.
  - Linear search is inefficient for large lists but works well for unsorted lists.
  - *[Code](Code/Searching/Linear_Search.py)*
  ![alt text](images/Linear_Search.png)
  ***
  </details>

  <details>
  <summary> Binary Search </summary>

  ## *Binary Search*
  - Binary search is a searching algorithm that works by repeatedly dividing the list in half and comparing the target element with the middle element.
  - The algorithm requires the list to be sorted in ascending order.
  - Binary search has a time complexity of O(log n) in the worst case, where n is the number of elements in the list.
  - Binary search is efficient for large lists and works well for sorted lists.
  - *[Code](Code/Searching/Binary_Search.py)*
  ![alt text](images/Binary_Search.png)
  ![alt text](images/Binary_Search2.png)
  ![alt text](images/Binary_Search3.png)
  ***
  </details>
***

# *Linked List*

- A linked list is a data structure that consists of a sequence of elements, where each element points to the next element in the sequence.
- Linked lists are dynamic data structures that can grow or shrink in size during program execution.
- Every element of a linked list is called a "node" and contains two parts: data and a reference to the next node in the sequence.
- Linked lists can be singly linked, doubly linked, or circular linked.

  <details>
  <summary> Singly Linked List </summary>

  ## *Singly Linked List*
  - A singly linked list is a type of linked list where each node points to the next node in the sequence.
  - The last node in the list points to a null reference.
  - Singly linked lists can be used to implement stacks, queues, and other data structures.
  - *[Code](Code/LinkedList/Singly_Linked_List.py)*
  ![alt text](images/Singly_Linked_List.png)
 

  ### *Singly Linked List Operations*
  
  - **Insertion**
    - *[Code](Code/LinkedList/Insertion_Singly_Linked_List.py)*
    <details>
    <summary> Insertion at the beginning of the list </summary>

    - Time Complexity: O(1)
      ![alt text](images/Insert_Beginning.png)
      ![alt text](images/Insert_Beginning2.png)
    </details>

    <details>
    <summary> Insertion at the end of the list </summary>

    - Time Complexity: O(n)
      ![alt text](images/Insert_End.png)
    </details>

    <details>
    <summary> Insertion at a specific position in the list </summary>

    - Time Complexity: O(n)
      ![alt text](images/Insert_Position.png)
      ![alt text](images/Insert_Position2.png)
    </details>

  - **Deletion**
    - *[Code](Code/LinkedList/Deletion_Singly_Linked_List.py)*
    <details>
    <summary> Deletion at the beginning of the list </summary>

    - Time Complexity: O(1)
      ![alt text](images/Delete_Beginning.png)
    </details>
    
    <details>
    <summary> Deletion at the end of the list </summary>

    - Time Complexity: O(n)
    </details>

    <details>
    <summary> Deletion at a specific position in the list </summary>

    - Time Complexity: O(n)
      ![alt text](images/Delete_Position.png)
    </details>
  </details>

  <details>
  <summary> Doubly Linked List </summary>

  ## *Doubly Linked List*
  - A doubly linked list is a type of linked list where each node points to both the next and previous nodes in the sequence.
  - The first node in the list points to a null reference, and the last node points to a null reference.
  - Doubly linked lists can be used to implement stacks, queues, and other data structures.
  - *[Code](Code/LinkedList/Doubly_Linked_List.py)*
  ![alt text](images/Doubly_Linked_List.png)

  ### *Doubly Linked List Operations*

  - **Insertion**
    - *[Code](Code/LinkedList/Insertion_Doubly_Linked_List.py)*
    <details>
    <summary> Insertion at the beginning of the list </summary>

    - Time Complexity: O(1)
      ![alt text](images/Insert_Beginning_Doubly.png)
      ![alt text](images/Insert_Beginning_Doubly2.png)
    </details>

    <details>
    <summary> Insertion at the end of the list </summary>

    - Time Complexity: O(n)
      ![alt text](images/Insert_End_Doubly.png)
      ![alt text](images/Insert_End_Doubly2.png)
    </details>

    <details>
    <summary> Insertion at a specific position in the list </summary>

    - Time Complexity: O(n)
      ![alt text](images/Insert_Position_Doubly.png)
      ![alt text](images/Insert_Position_Doubly2.png)
    </details>
  
  - **Deletion**
    - *[Code](Code/LinkedList/Deletion_Doubly_Linked_List.py)*
    <details>
    <summary> Deletion at the beginning of the list </summary>

    - Time Complexity: O(1)
      ![alt text](images/Delete_Beginning_Doubly.png)
    </details>

    <details>
    <summary> Deletion at the end of the list </summary>

    - Time Complexity: O(n)
      ![alt text](images/Delete_End_Doubly.png)
    </details>

    <details>
    <summary> Deletion at a specific position in the list </summary>

    - Time Complexity: O(n)
      ![alt text](images/Delete_Position_Doubly.png)
      ![alt text](images/Delete_Position_Doubly2.png)
    </details>

  </details>

  <details>
  <summary> Circular Linked List </summary>
  
  ## *Circular Linked List*
  - A circular linked list is a type of linked list where the last node points back to the first node in the sequence.
  - Circular linked lists can be used to implement circular buffers, scheduling algorithms, and other data structures.
  - *[Code](Code/LinkedList/Circular_Linked_List.py)*
  ![alt text](images/Circular_Linked_List.png)

  ### *Circular Linked List Operations*

  - **Insertion**
    - *[Code](Code/LinkedList/Insertion_Circular_Linked_List.py)*
    <details>
    <summary> Insertion at the beginning of the list </summary>

    - Time Complexity: O(1)
      ![alt text](images/Insert_Beginning_Circular.png)
    </details>

    <details>
    <summary> Insertion at the end of the list </summary>

    - Time Complexity: O(n)
      ![alt text](images/Insert_End_Circular.png)
    </details>

    <details>
    <summary> Insertion at a specific position in the list </summary>

    - Time Complexity: O(n)
      ![alt text](images/Insert_Position_Circular.png)
      ![alt text](images/Insert_Position_Circular2.png)
    </details>

  - **Deletion**
    - *[Code](Code/LinkedList/Deletion_Circular_Linked_List.py)*
    <details>
    <summary> Deletion at the beginning of the list </summary>

    - Time Complexity: O(1)
      ![alt text](images/Delete_Beginning_Circular.png)
      ![alt text](images/Delete_Beginning_Circular2.png)
    </details>

    <details>
    <summary> Deletion at the end of the list </summary>

    - Time Complexity: O(n)
      <!-- ![alt text](images/Delete_End_Circular.png) -->
    </details>

    <details>
    <summary> Deletion at a specific position in the list </summary>

    - Time Complexity: O(n)
      ![alt text](images/Delete_Position_Circular.png)
      ![alt text](images/Delete_Position_Circular2.png)
    </details>
  </details>
***

# *Stack*

- A stack is a data structure that stores elements in a last-in, first-out (LIFO) order.
- Stacks can be implemented using arrays or linked lists.
- Stacks are used in many applications, such as function call management, expression evaluation, and backtracking algorithms.
- All stack operations have a time complexity of O(1).

  <details>
  <summary>Stack Operations</summary>

  ## *Stack Operations*
  - **Push**
    - The `push()` operation adds an element to the top of the stack.
    

  - **Pop**
    - The `pop()` operation removes and returns the element at the top of the stack.

  - **Peek**
    - The `peek()` operation returns the element at the top of the stack without removing it.

  - **isFull**
    - The `isFull()` operation checks if the stack is full.

  - **Size**
    - The `size()` operation returns the number of elements in the stack. 
  </details>
--- 

# *Queue*

- A queue is a data structure that stores elements in a first-in, first-out (FIFO) order.
- Queues can be implemented using arrays or linked lists.
- Queues are used in many applications, such as task scheduling, breadth-first search, and printer spooling.
- All queue operations have a time complexity of O(1).

  <details>
  <summary>Queue Operations</summary>

  ## *Queue Operations*
  - **Enqueue**
    - The `enqueue()` operation adds an element to the back of the queue.
    
  - **Dequeue**
    - The `dequeue()` operation removes and returns the element at the front of the queue.

  - **Peek**
    - The `peek()` operation returns the element at the front of the queue without removing it.

  - **isEmpty**
    - The `isEmpty()` operation checks if the queue is empty.

  - **Size**
    - The `size()` operation returns the number of elements in the queue. 
  </details>

---

# *Circular Queue*

- A circular queue is a data structure that stores elements in a circular order.
- Circular queues can be implemented using arrays or linked lists.
- Circular queues are used in many applications, such as CPU scheduling, memory management, and disk scheduling.

  <details>
  <summary>Circular Queue Operations</summary>

  ## *Circular Queue Operations*
  - **Enqueue**
    - The `enqueue()` operation adds an element to the back of the queue.
    
  - **Dequeue**
    - The `dequeue()` operation removes and returns the element at the front of the queue.

  - **Peek**
    - The `peek()` operation returns the element at the front of the queue without removing it.

  - **isFull**
    - The `isFull()` operation checks if the queue is full.

  - **isEmpty**
    - The `isEmpty()` operation checks if the queue is empty.

  - **Size**
    - The `size()` operation returns the number of elements in the queue. 
  </details>
---

# *Hashing*

- Hashing is the process of transforming a key into a hash value using a hash function.
- Hashing is used to store and retrieve data in a data structure called a hash table.
- Hash tables are used in many applications, such as database indexing, caching, and password storage.
- *[Code](Code/Hashing/Hashing.py)*

  <details>
  <summary>Hash Function</summary>

  ## *Hash Function*
  - A hash function is a function that takes an input (or "key") and returns a fixed-size value (or "hash value").
  - Hash functions are used to map keys to hash values in a hash table.
  - A good hash function should be deterministic, efficient, and distribute keys evenly across the hash table.
  ---
  </details>
  <details>
  <summary>Hash Table</summary>

  ## *Hash Table*
  - A hash table is a data structure that stores key-value pairs in an array.
  - Hash tables use a hash function to map keys to hash values, which are used to index the array.
  - Hash tables are used to implement associative arrays, sets, and other data structures.

  ### *Hash Table Operations*
  
  - **Insert**
    - The `insert()` operation adds a key-value pair to the hash table.

  - **Search**
    - The `search()` operation retrieves the value associated with a key in the hash table.
  
  - **Delete**
    - The `delete()` operation removes a key-value pair from the hash table.
  ---
  </details>

  <details>
  <summary>Hashing Collision</summary>  

  ## *Hashing Collision*
  - Hashing collision occurs when two or more keys map to the same hash value in a hash table.
  - Collision resolution techniques are used to handle collisions and ensure that keys are stored and retrieved correctly.

  ### *Collision Resolution Techniques*

  <details>
  <summary>Chaining</summary>

  - **Chaining**
    - Chaining is a collision resolution technique that uses linked lists to store key-value pairs with the same hash value.
    - Chaining has a time complexity of O(1) for insert, search, and delete operations.
    - Chaining is efficient for large hash tables and handles collisions well.
    - *[Code](Code/Hashing/Chaining.py)*
    ![alt text](images/Chaining.png)
    ![alt text](images/Chaining2.png)
  </details>

  <details>
  <summary>Linear Probing</summary>

  - **Linear Probing**
    - Linear probing is an open addressing technique that resolves collisions by searching for the next available slot in the hash table.
    - Linear probing has a time complexity of O(1) for insert and search operations and O(n) for delete operations.
    - Linear probing is efficient for small hash tables but may lead to clustering.
    - *[Code](Code/Hashing/Linear_Probing.py)*
    ![alt text](images/Linear_Probing.png)
    ![alt text](images/Linear_Probing2.png)
  </details>

  <details>
  <summary>Quadratic Probing</summary>
  
  - **Quadratic Probing**
    - Quadratic probing is an open addressing technique that resolves collisions by using a quadratic function to search for the next available slot in the hash table.
    - Quadratic probing has a time complexity of O(1) for insert and search operations and O(n) for delete operations.
    - Quadratic probing is efficient for small hash tables but may lead to clustering.
    - *[Code](Code/Hashing/Quadratic_Probing.py)*
  </details>

  <details>
  <summary>Double Hashing</summary>  

  - **Double Hashing**  
    - Double hashing is an open addressing technique that resolves collisions by using a second hash function to search for the next available slot in the hash table.
    - Double hashing has a time complexity of O(1) for insert and search operations and O(n) for delete operations.
    - Double hashing is efficient for small hash tables and avoids clustering.
    - *[Code](Code/Hashing/Double_Hashing.py)*
  </details>

  <details>
  <summary>Rehashing</summary>

  - **Rehashing**
    - Rehashing is a technique that increases the size of the hash table and rehashes all key-value pairs when the load factor exceeds a certain threshold.
    - Rehashing reduces the likelihood of collisions and improves the performance of the hash table.
    - *[Code](Code/Hashing/Rehashing.py)*
    ![alt text](images/Rehashing.png)
  </details>
  
  ---
  </details>
---

# *String Matching Algorithms*

- String matching algorithms are used to find the occurrence of a pattern within a text.
- There are many different string matching algorithms that can be used to search for a pattern in a text.

  <details>
  <summary>Brute Force Algorithm</summary>

  ## *Brute Force Algorithm*
  - The brute force algorithm is a simple string matching algorithm that compares the pattern with substrings of the text.
  - The algorithm slides the pattern over the text one character at a time and checks for a match.
  - The brute force algorithm has a time complexity of O(mn) in the worst case, where m is the length of the pattern and n is the length of the text.
  - The brute force algorithm is inefficient for large texts and patterns.
  - *[Code](Code/String_Matching/Brute_Force.py)*
  ![alt text](images/Brute_Force.png)
  ![alt text](images/Brute_Force2.png)
  ![alt text](images/Brute_Force3.png)
  ---
  </details>

  <details>
  <summary>Rabin-Karp Algorithm</summary>

  ## *Rabin-Karp Algorithm*
  - The Rabin-Karp algorithm is a string matching algorithm that uses hashing to compare the pattern with substrings of the text.
  - The algorithm computes the hash value of the pattern and compares it with the hash value of substrings of the text.
  - The Rabin-Karp algorithm has a time complexity of O(mn) in the worst case, where m is the length of the pattern and n is the length of the text.
  - The Rabin-Karp algorithm is efficient for large texts and patterns.
  - *[Code](Code/String_Matching/Rabin_Karp.py)*
  


***

# *Tree*
- A tree is a non linear data structure that consists of nodes connected by edges.
- Trees are used to represent hierarchical relationships between elements.
- Relationships between nodes in a tree are defined by parent-child relationships.
- The top node in a tree is called the root node, and nodes without children are called leaf nodes.
![alt text](images/Tree.png)
- Trees can be used to implement binary search trees, expression trees, and other data structures.
- *Depth of a  Node*
  - The depth of a node is the number of edges from the root to the node.
  ![alt text](images/Depth_Tree.png)
- *Height of a Node*
  - The height of a node is the number of edges on the longest path from the node to a leaf.
  ![alt text](images/Height_Tree.png)
- *Degree of a Node*
  - The degree of a node is the number of children of the node.
  ![alt text](images/Degree_Tree.png)
- *Level of a Node*
  - The level of a node is the depth of the node.
  ![alt text](images/Level_Tree.png)