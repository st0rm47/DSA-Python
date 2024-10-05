# Creation of Trees

class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        print(f"Tree created with data {self.data}")
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        print (f"Added {child.data} as child of {self.data}")

def build_tree():
    root = Tree("Electronics")
    
    laptop = Tree("Laptop")
    laptop.add_child(Tree("Mac"))
    laptop.add_child(Tree("Surface"))
    laptop.add_child(Tree("Thinkpad"))
    
    cellphone = Tree("Cellphone")
    cellphone.add_child(Tree("iPhone"))
    cellphone.add_child(Tree("Google Pixel"))
    cellphone.add_child(Tree("Samsung Galaxy"))
    
    tv = Tree("TV")
    tv.add_child(Tree("Samsung"))
    tv.add_child(Tree("LG"))
    tv.add_child(Tree("Sony"))
    
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    return root

def get_level(root, level):
    if root is None:
        return
    if level == 0:
        print(root.data)
        return 
    for child in root.children:
        get_level(child, level-1)

        
root = build_tree()
for i in range(3):
    print(f"Level {i}")
    get_level(root, i)
    print()


