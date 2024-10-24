# AVL Trees

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
        
        """ 
        The height of a node is the maximum of the height of the left child and the height of the right child, plus 1.
        """
    
class AVLTree:
    def __init__(self):
        self.root = None
        
    def getHeight(self, node):
        if not node:
            return 0
        return node.height
    
    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def inorder_search(self, root):
        if root:
            self.inorder_search(root.left)
            print(root.data, end=' ')
            self.inorder_search(root.right)
            
    def rotateLeft(self, node):
        rightChild = node.right
        leftChild = rightChild.left
        
        rightChild.left = node
        node.right = leftChild
        
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        rightChild.height = 1 + max(self.getHeight(rightChild.left), self.getHeight(rightChild.right))
        """ 
        The height of a node is the maximum of the height of the left child and the height of the right child, plus 1.
        """
        return rightChild
        
    def rotateRight(self, node):
        leftChild = node.left
        rightChild = leftChild.right
        
        leftChild.right = node
        node.left = rightChild
        
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        leftChild.height = 1 + max(self.getHeight(leftChild.left), self.getHeight(leftChild.right))
        return leftChild
    
    def insert(self, root, data):
        if not root:
            return AVLNode(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
          
        # Update the height of the root 
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        # Get the balance factor of the root
        balance = self.getBalance(root)
        
        # If the root is unbalanced, then there are 4 cases
        # 1. Left-Left Case
        if balance > 1 and data < root.left.data:
            return self.rotateRight(root)
        
        # 2. Right-Right Case
        if balance < -1 and data > root.right.data:
            return self.rotateLeft(root)
        
        # 3. Left-Right Case
        if balance > 1 and data > root.left.data:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        
        # 4. Right-Left Case
        if balance < -1 and data < root.right.data:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
        
        return root
        
        
    def delete(self, root, data):
        if not root:
            return root
        elif data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        
        if root is None:
            return root
        
        # Update the height of the root
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        # Get the balance factor of the root
        balance = self.getBalance(root)
        
        # If the root is unbalanced, then there are 4 cases
        # 1. Left-Left Case
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rotateRight(root)
        
        # 2. Right-Right Case
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.rotateLeft(root)
        
        # 3. Left-Right Case
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        
        # 4. Right-Left Case
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
        
        return root
    
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)
    
    def search(self, root, data):
        if root is None or root.data == data:
            return root
        if root.data < data:
            return self.search(root.right, data)
        return self.search(root.left, data)
    
    def getMinValue(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

# Driver code
avl = AVLTree()
values = [9, 5, 10, 0, 6, 11, -1, 1, 2] 
for value in values:
    avl.root = avl.insert(avl.root, value)
avl.inorder_search(avl.root)
print()
avl.root = avl.delete(avl.root, 10)
avl.inorder_search(avl.root)
print()
avl.root = avl.delete(avl.root, 1)
avl.inorder_search(avl.root)
print()