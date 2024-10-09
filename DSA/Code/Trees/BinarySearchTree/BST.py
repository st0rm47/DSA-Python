class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class Bst:
    def __init__(self):
        self.root = None
         
    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

        """
        - Here we are inserting a key in the BST
        - If the root is None we return a new node with the key
        - If the key is greater than the root value we insert in the right subtree
        - If the key is less than the root value we insert in the left subtree
        
        """

    def search(self,root, key):
        if root is None:
            return None
        
        if root.val == key:
            return root
        elif root.val < key:
            return self.search(root.right, key)
        else:
            return self.search(root.left, key)
        
        """
        - Here we are searching for a key in the BST
        - If the key is found we return the node
        - If the key is not found we return None
        - If the key is greater than the root value we search in the right subtree
        - If the key is less than the root value we search in the left subtree
        """
        
    def delete (self,root, key):
        if root is None:
            return root
        
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
                """
                - If the node has only one child or no child
                - We store the child in a temporary variable
                - We delete the node
                - We return the child
                """
            temp = self.minValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
            """
            - If the node has two children
            - We find the inorder successor of the node
            - We copy the inorder successor's value to the node
            - We delete the inorder successor    
            """
        return root

    def minValueNode(self,node):
        current = node
        while current.left is not None:
            current = current.left
        return current
        """
        - This function finds the inorder successor of a node
        - The inorder successor is the node with the smallest value in the right subtree
        - We keep moving to the left child of the node until we reach the leftmost node
        - We return the leftmost node
        """

    def inorder(self,root, traversal = []):
        traversal = []
            
        if root:
            traversal+=self.inorder(root.left, traversal)
            traversal.append(root.val)
            traversal+=self.inorder(root.right, traversal)
        return traversal
        """
        - This function performs inorder traversal of the BST
        - We first visit the left child
        - We then visit the root
        - We finally visit the right child
        - We return the traversal list
        """
    
    def smallest (self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.val
        """
        - This function finds the smallest value in the BST
        - We keep moving to the left child of the node until we reach the leftmost node
        - We return the value of the leftmost node
        """
    
    def lca(self, root, n1, n2):
        if root is None:
            return None
        
        if root.val < n1 and root.val < n2:
            return self.lca(root.right, n1, n2)
        
        if root.val > n1 and root.val > n2:
            return self.lca(root.left, n1, n2)
        
        return root
        """
        - This function finds the lowest common ancestor of two nodes in the BST
        - If the root value is greater than both the nodes we search in the left subtree
        - If the root value is less than both the nodes we search in the right subtree
        - If the root value is between the two nodes we return the root
        """

node = Node(8)
bst = Bst()
bst.root = node
bst.insert(bst.root, 6)
bst.insert(bst.root, 10)
bst.insert(bst.root, 5)
bst.insert(bst.root, 7)
bst.insert(bst.root, 9)
bst.insert(bst.root, 11)
print("Inorder traversal before deletion:", bst.inorder(bst.root))
print("Lowest common ancestor of 5 and 9:", bst.lca(bst.root, 5, 9).val)
print("Searching for node 6:", bst.search(bst.root, 6).val)
bst.delete(bst.root, 6)
bst.delete(bst.root, 8)
print("Inorder traversal after deletion:", bst.inorder(bst.root))
print("Searching for node 6 after deletion:", bst.search(bst.root, 6))
print("Smallest value in the BST:", bst.smallest(bst.root))
