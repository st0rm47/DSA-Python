class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Node(data)
                print(f"Added {data} as left child of {self.data}")
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Node(data)
                print(f"Added {data} as right child of {self.data}")

def build_tree():
    root = Node(10)
    root.add_child(5)
    root.add_child(15)
    root.add_child(3)
    root.add_child(7)
    root.add_child(12)
    root.add_child(18)
    return root

class BinaryTree:
    def __init__(self, root = None):
        self.root = root
                    
    def preorder_traversal(self,node, traversal=[]):
        if not node:
            return traversal
        traversal.append(node.data)
        self.preorder_traversal(node.left, traversal)
        self.preorder_traversal(node.right, traversal)
        return traversal

    def postorder_traversal(self,node, traversal=[]):
        if not node:
            return traversal
        self.postorder_traversal(node.left, traversal)
        self.postorder_traversal(node.right, traversal)
        traversal.append(node.data)
        return traversal

    def inorder_traversal(self,node, traversal=[]):
        if not node:
            return traversal
        self.inorder_traversal(node.left, traversal)
        traversal.append(node.data)
        self.inorder_traversal(node.right, traversal)
        return traversal

    def levelorder_traversal(self,node):
        if not node:
            return
        queue = [node]
        traversal = []
        while len(queue) > 0:
            traversal.append(queue[0].data)
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return traversal
    

if __name__ == "__main__":
    root = build_tree()
    binary_tree = BinaryTree(root)
    print(binary_tree.preorder_traversal(root))
    print(binary_tree.postorder_traversal(root))
    print(binary_tree.inorder_traversal(root))
    print(binary_tree.levelorder_traversal(root))


