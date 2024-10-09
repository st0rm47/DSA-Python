class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add (self, data):
        if self.data == data:
            return
        if self.data > data:
            if self.left:
                self.left.add(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = Node(data)
                
class Binary_Tree:
    def __init__(self):
        self.root = None
        
    def is_perfect_tree(self, root):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is not None and root.right is not None:
            return self.is_perfect_tree(root.left) and self.is_perfect_tree(root.right)
        return False
    
        """
        Here if there is a node with only one child, then it is not a perfect binary tree.
        If there is a node with no child, then it is a perfect binary tree.
        So, we check if the node has both children, then we recursively check for the left and right subtrees.
        """

if __name__ == '__main__':
    tree = Binary_Tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    print(tree.is_perfect_tree(tree.root))
    tree.root.right.right.right = Node(8)
    print(tree.is_perfect_tree(tree.root))
    tree.root.right.right.right.left = Node(9)
    print(tree.is_perfect_tree(tree.root))
    tree.root.right.right.right.right = Node(10)
    print(tree.is_perfect_tree(tree.root))
    tree.root.right.right.right.right.right = Node(11)
    print(tree.is_perfect_tree(tree.root))
    tree.root.right.right.right.right.right.left = Node(12)
    print(tree.is_perfect_tree(tree.root))
    tree.root.right.right.right.right.right.right = Node(13)
    print(tree.is_perfect_tree(tree.root))
    tree.root.right.right.right.right.right.right.left = Node(14)
    print(tree.is_perfect_tree(tree.root))
    tree.root.right.right.right.right.right.right.right = Node(15)
    print(tree.is_perfect_tree(tree.root))
    tree.root.right.right.right.right.right.right.right.left = Node(16)
    print(tree.is_perfect_tree(tree.root))
    tree.root.right.right.right.right.right.right.right.right = Node(17)
    print(tree.is_perfect_tree(tree.root))
    tree.root.right.right.right.right.right.right.right.right.left = Node(18)
    print(tree.is_perfect_tree(tree.root))
    tree.root.right.right.right.right.right.right.right.right.right = Node(19)
    print(tree.is_perfect_tree(tree.root))
    tree.root.right.right.right.right.right.right.right.right.right.left = Node(20)
    print(tree.is_perfect_tree(tree.root))
    tree.root