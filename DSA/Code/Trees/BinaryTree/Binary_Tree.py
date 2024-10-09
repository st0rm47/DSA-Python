# Implementation of Binary Tree

class Binary_Tree:
    def __init__(self, data, is_root=False):
        self.data = data    # Root Node
        self.left = None    # Left Child
        self.right = None   # Right Child
        if is_root:
            print(f"Root Node: {self.data}")
        
    def add_child(self,data):
        if data == self.data:
            return
        
        if data < self.data:   
            if self.left:  
                self.left.add_child(data) 
            else:  
                self.left = Binary_Tree(data)
                print(f"Added {data} as left child of {self.data}")
                
                """ 
                - Add data in the left subtree if it is less than the root node. 
                - If the left child exists, then add the data in the left subtree. 
                - Otherwise, create a new node and add the data in the left subtree. 
                """       
                    
        else:                 
            if self.right:     
                self.right.add_child(data)
            else:
                self.right = Binary_Tree(data)
                print(f"Added {data} as right child of {self.data}")
        
                """ 
                - Add data in the right subtree if it is greater than the root node.
                - If the right child exists, then add the data in the right subtree. 
                - Otherwise, create a new node and add the data in the right subtree. 
                """
                 
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
                """
                - If the value is found in the root node, return True.
                - If the value is less than the root node, search in the left subtree.
                - If the value is greater than the root node, search in the right subtree.
                - If the value is not found in the tree, return False.
                """
    
    def delete (self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self
    
        """
        - If the value is less than the root node, delete the value from the left subtree.
        - If the value is greater than the root node, delete the value from the right subtree.
        - If the value is found in the root node, then:
            - If the root node has no children, return None.
            - If the root node has no left child, return the right child.
            - If the root node has no right child, return the left child.
            - If the root node has both children, find the minimum value in the right subtree, replace the root node with the minimum value, and delete the minimum value from the right subtree.
            - Return the root node.
            - If the value is not found in the tree, return the root node.                          
        """
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
        
        """
        - Find the minimum value in the tree.
        - If the left child is None, return the root node.
        - Otherwise, recursively find the minimum value in the left subtree.
        """

        
binarytree= Binary_Tree(10, is_root=True)
binarytree.add_child(5)
binarytree.add_child(15)
binarytree.add_child(3)
binarytree.add_child(7)
binarytree.add_child(12)
binarytree.add_child(18)
binarytree.add_child(17)
binarytree.add_child(20)
print(binarytree.search(15))
print(binarytree.search(10))
print(binarytree.search(100))
binarytree.delete(15)
print(binarytree.search(15))
binarytree.delete(10)
print(binarytree.search(10))
