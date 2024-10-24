# Balanced Binary Trees

#Rotations
# 1. Left Rotation
# 2. Right Rotation
# 3. Left-Right Rotation
# 4. Right-Left Rotation

def rotateLeft(node):
    # Left child of the right child
    leftChild = rightChild.left
    # Right child of the node
    rightChild = node.right

    # Perform rotation
    rightChild.left = node
    node.right = leftChild

    return rightChild

def rotateRight(node):
    # Right child of the left child
    rightChild = leftChild.right
    # Left child of the node
    leftChild = node.left

    # Perform rotation
    leftChild.right = node
    node.left = rightChild

    return leftChild

def rotateLeftRight(node):
    # Left child of the right child
    leftChild = rightChild.left
    # Right child of the left child
    rightChild = leftChild.right

    # Perform rotation
    leftChild.right = rightChild
    rightChild.left = leftChild

    node.right = leftChild
    leftChild = node.right

    return leftChild

def rotateRightLeft(node):
    # Right child of the left child
    rightChild = leftChild.right
    # Left child of the right child
    leftChild = rightChild.left

    # Perform rotation
    rightChild.left = leftChild
    leftChild.right = rightChild

    node.left = rightChild
    rightChild = node.left
    
    return rightChild

