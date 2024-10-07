#Post-order Traversal Example

class TreeNode:
    def __init__(self, data, size=0):
        self.data = data
        self.size = size
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, root=None):
        self.root = root

    def calculate_disk_space(self, node):
        total_size = node.size
        for child in node.children:
            total_size += self.calculate_disk_space(child)
        return total_size

# create the tree nodes (directories and files)
my_documents = TreeNode("MyDocuments")
music = TreeNode("Music")
pictures = TreeNode("Pictures")
work = TreeNode("Work", 10)  # Work is a file, so it has a size
m1 = TreeNode("M1", 20)  # M1 is a file, so it has a size
m2 = TreeNode("M2", 10)  # M2 is a file, so it has a size
p1 = TreeNode("P1", 30)  # P1 is a file, so it has a size
p2 = TreeNode("P2", 20)  # P2 is a file, so it has a size

# build the tree structure
music.add_child(m1)
music.add_child(m2)
pictures.add_child(p1)
pictures.add_child(p2)
my_documents.add_child(music)
my_documents.add_child(pictures)
my_documents.add_child(work)

# create the tree
tree = Tree(my_documents)

# calculate the total disk space
total_size = tree.calculate_disk_space(my_documents)
print(f"{total_size} GB")