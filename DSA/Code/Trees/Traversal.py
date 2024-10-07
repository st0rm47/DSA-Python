class Node:
    def __init__(self,data):
        self.data = data
        self.children = []
        
    def add_child(self,child):
        self.children.append(child)
    
def build_tree():
    root = Node("Root")
    child1 = Node("Left")
    child2 = Node("Right")
    root.add_child(child1)
    root.add_child(child2)
    return root

# Pre-order Traversal
def preorder_traversal(node,traversal= []):
    if not node:
        return traversal
    #Add the root node first
    traversal.append(node.data)
    
    #Recursively transverse the left subtree
    for child in node.children:
        preorder_traversal(child,traversal)
    
    return traversal
    
    """
    Visit the root node and add it to the traversal list.
    Recursively call the function for the left child.
    After finishing the left subtree, call the function for the right child
    """
    
#Post-order Traversal
def postorder_traversal(node,traversal = []):
    if not node:
        return traversal
    
    #Recursively transverse the left subtree
    for child in node.children:
        postorder_traversal(child,traversal)
    
    #Add the root node last
    traversal.append(node.data)
    
    return traversal

    """
    Recursively call the function for the left child.
    After finishing the left subtree, call the function for the right child
    Visit the root node and add it to the traversal list.
    """

#Level-order Traversal  (Breadth First Search)
def levelorder_traversal(node):
    if not node:
        return
    
    queue = [node]
    traversal = []
    
    while len(queue) > 0:
        traversal.append(queue[0].data)
        node = queue.pop(0)
        
        for child in node.children:
            queue.append(child)
            
    return traversal

    """
    Create a queue and add the root node to it.
    While the queue is not empty, remove the first node from the queue.
    Add the node to the traversal list.
    Add all the children of the node to the queue.
    """

#In-order Traversal
def inorder_traversal(node,traversal = []):
    if not node:
        return traversal
    
    if len(node.children) > 1:
        inorder_traversal(node.children[0],traversal)
    
    traversal.append(node.data)
    
    if len(node.children) > 1:
        inorder_traversal(node.children[1],traversal)
    
    return traversal

    """
    Recursively call the function for the left child.
    Visit the root node and add it to the traversal list.
    Recursively call the function for the right child.
    """


root = build_tree()
print(preorder_traversal(root))
print(postorder_traversal(root))
print(levelorder_traversal(root))
print(inorder_traversal(root))  



