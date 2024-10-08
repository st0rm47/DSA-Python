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
                
                """ Add data in the left subtree if it is less than the root node. 
                If the left child exists, then add the data in the left subtree. 
                Otherwise, create a new node and add the data in the left subtree. """       
                    
        else:                 
            if self.right:     
                self.right.add_child(data)
            else:
                self.right = Binary_Tree(data)
                print(f"Added {data} as right child of {self.data}")
        
                """ Add data in the right subtree if it is greater than the root node.
                If the right child exists, then add the data in the right subtree. 
                Otherwise, create a new node and add the data in the right subtree. """
        
binarytree= Binary_Tree(10, is_root=True)
binarytree.add_child(5)
binarytree.add_child(15)
binarytree.add_child(3)
binarytree.add_child(7)
binarytree.add_child(12)
binarytree.add_child(18)
