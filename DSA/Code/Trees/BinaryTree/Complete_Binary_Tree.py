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
        
    def is_complete_tree(self, root):
        if root is None:
            return True
        queue = []
        queue.append(root)
        
        # This flag is used to indicate if we have encountered a node with missing children
        flag = False
        
        while queue:
            temp = queue.pop(0)

            # Check the left child
            if temp.left:
                # If we have already encountered a node with missing children, the tree is incomplete
                if flag:
                    return False
                queue.append(temp.left)  # Add the left child to the queue
            else:
                # If there is no left child, set the flag to True
                flag = True
            
            # Check the right child
            if temp.right:
                # If the flag is already set, and we find a right child, it's incomplete
                if flag:
                    return False
                queue.append(temp.right)  # Add the right child to the queue
            else:
                # If there is no right child, set the flag to True
                flag = True
        return True

    """
    - We use level-order traversal (using a queue) to check if the tree is complete.
    - The `flag` is used to ensure that once a node has missing children, all nodes afterward must be leaf nodes.
    - If we encounter a child after the `flag` is set, the tree is incomplete and we return False.
    - If no invalid structure is found during traversal, the tree is complete, and we return True.
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
    print(tree.is_complete_tree(tree.root))
    tree.root.right.right.right = Node(8)
    print(tree.is_complete_tree(tree.root))
    tree.root.right.right.right.left = Node(9)
    print(tree.is_complete_tree(tree.root))
    tree.root.right.right.right.right = Node(10)
    print(tree.is_complete_tree(tree.root))
    tree.root.right.right.right.right.right = Node(11)
    print(tree.is_complete_tree(tree.root))
    tree.root.right.right.right.right.right.left = Node(12)
    print(tree.is_complete_tree(tree.root))
    tree.root.right.right.right.right.right.right = Node(13)
    print(tree.is_complete_tree(tree.root))
    tree.root.right.right.right.right.right.right.left = Node(14)
    print(tree.is_complete_tree(tree.root))
