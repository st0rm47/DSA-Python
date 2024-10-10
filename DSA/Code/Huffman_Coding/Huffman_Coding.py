class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def add_left(self, node):
        self.left = node
    
    def add_right(self, node):
        self.right = node
        
class HuffmanTree:
    def __init__(self):
        self.root = None
        
    def build_tree(self, freq_map):
        
        # Count the frequency of each character in the input string
        freq_map = {char:s.count(char) for char in s}
    
        # Create a leaf node for each character in the frequency map
        huffman_tree = [HuffmanNode(char, freq) for char, freq in freq_map.items()] 
        
        # Create a heap from the leaf nodes
        while len(huffman_tree) > 1:
            
            # Sort the heap based on the frequency of the nodes
            huffman_tree = sorted(huffman_tree, key=lambda x: x.freq)
            
            # Pop the two nodes with the lowest frequency
            left = huffman_tree.pop(0)
            right = huffman_tree.pop(0)
            
            # Create a new node with the sum of the frequencies of the two nodes
            parent = HuffmanNode(None, left.freq + right.freq)
            parent.add_left(left)
            parent.add_right(right)
            
            # Add the new node to the tree
            huffman_tree.append(parent)
        
        # The root of the tree is the only node left in the heap
        self.root = huffman_tree[0]
        
    
    def get_codes(self, node = None, code = "", codes ={}):
        # If we are at the root node, initialize the code dictionary
        if node is None:
            node = self.root
            codes = {}
        
        # If we are at a leaf node, add the code to the dictionary
        if node.char is not None:
            codes[node.char] = code
            return codes
        
        # Traverse the left subtree
        self.get_codes(node.left, code + "0", codes)
        
        # Traverse the right subtree
        self.get_codes(node.right, code + "1", codes)
        
        return codes
        
    def encode(self, text):
        # Get the codes for each character in the tree
        codes = self.get_codes()
        encoded_text = ""
        # Encode the text using the codes
        for char in text:
            encoded_text +=codes[char]
        return encoded_text
    
    def decode(self, encoded_text):
        decoded_text = ""
        node = self.root
        for bit in encoded_text:
            # Traverse the tree based on the bits in the encoded text
            if bit == "0":
                node = node.left
            else:
                node = node.right
            
            # If we reach a leaf node, add the character to the decoded text
            if node.char is not None:
                decoded_text += node.char
                node = self.root
        
        return decoded_text
    
s = "hello world"
tree = HuffmanTree()
tree.build_tree(s)
encoded_text = tree.encode(s)
decoded_text = tree.decode(encoded_text)
print(encoded_text)
print(decoded_text)


