from huffMap import HuffMap
from huffTree import HuffTree
from huffPQ import HuffPQ


class Huffman:
    """
    This Huffman class does the following:
      1. Compresses a passed in string of characters from a text file:
         - build the character frequency map of HuffElements
         - build the Huffman Tree using the HuffPQ of HuffTrees
         - recursively walk the Huffman tree assigning the 
           correct binary code to each leaf HuffNode which contain
           the HuffElement for the character  
         - build the Huffman encoded binary string by retrieving the
           correct code from the HuffElements for each character
           in the file string
      2. Decompresses the encoded binary string
         - each binary character (0 or 1) is retrieved from the
           binary encoded string and used to walk the Huffman tree 
         - traverse the Huffman tree starting from the root going left 
           with '0' and right with '1' until you find a leaf node
         - retrieve the file string character from the HuffElement 
           in the HuffNode and add it to the output string.
    """
    def __init__(self):
        """
        Constructor: Create the Huffman class object
        Initialize the huff_map instance variable to a HuffMap
        Initialize the huffTree instance variable to None
        """
        self.huff_map = HuffMap()
        self.huff_tree = None

    def build_huff_map(self, file_str):
        """
        Populate the huffMap from the passed in file string:
         - keys: file characters
         - values: HuffElements holding character frequency counts
         
        Loop though each character in the file string
          1. If the huffMap does not contain the character, 
             add the character to the map
          2. Retrieve the HuffElement from the map and increment 
             the frequency
        """
        for char in file_str:
            if not self.huff_map.contains_char(char):
                self.huff_map.add_char(char)
            huff_element = self.huff_map.get_huff_elem(char)
            huff_element.inc_freq()

    def build_huff_tree(self):
        """
        1. Create an empty Huff Priority Queue: HuffPQ
        2. Create the set of character keys from the HuffMap
        3. Build a forest of HuffTrees one from each 
           HuffElement in the HuffMap using the character key 
           set to retrieve the HuffElements and enqueue each 
           single node HuffTree to the HuffPQ
        4. Loop through the HuffPQ min heap, dequeueing the two  
           lowest frequency count HuffTrees and combine them into 
           a new HuffTree, enqueueing the new single HuffTree back 
           to the HuffPQ and repeating until there is only one 
           HuffTree in the HuffPQ
        5. Dequeue the single HuffTree from the HuffPQ 
           and set it to the HuffTree instance variable
        """
        huff_pq = HuffPQ()
        char_key_set = self.huff_map.get_char_set()

        for char in char_key_set:
            huff_element = self.huff_map.get_huff_elem(char)
            huff_tree = HuffTree(huff_element)
            huff_pq.enqueue(huff_tree)

        while len(huff_pq) > 1:
            tree1 = huff_pq.dequeue()
            tree2 = huff_pq.dequeue()
            huff_pq.enqueue(HuffTree(None, left_tree=tree1, right_tree=tree2))

        self.huff_tree = huff_pq.dequeue()

    def build_huff_codes(self, root):
        """
        This is the helper function for the recursive assign_code
        method that walks the Huffman Tree (self.huff_tree)
        building the code for each character in the file string
        starting from the root of the Huffman Tree.
        
        If the passed in root is not None, call assign_code
        """
        if root is not None:
            self.assign_code(root)

    def assign_code(self, root):
        """
        Recursively get the binary bits for the code as you
        walk the Huffman Tree to the leaf node.
        The base case is when the left subtree of the root is None
        1. Get the code from the root HuffNode and add '0' to it
           Set this new code in the HuffNode of the left subtree 
           of root, and then call assign_code passing in the
           left subtree of root
        2. Get the code from the root HuffNode and add '1' to it
           Set this new code in the HuffNode of the right subtree 
           of root, and then call assign_code passing in the
           right subtree of root 
        """
        if root.left is not None:
            left_code = root.get_code()
            left_code += '0'
            root.left.set_code(left_code)
            self.assign_code(root.left)

            right_code = root.get_code()
            right_code += '1'
            root.right.set_code(right_code)
            self.assign_code(root.right)

    def build_binary_str(self, file_str):
        """
        Builds a binary string of ones and zeros by walking through 
        the passed in file_str and replacing each character with the 
        code in the HuffElement which is retrieved from the HuffMap
        Return the binary string
        """
        binary_string = ""
        for i in range(len(file_str)):
            char = file_str[i]
            huff_element = self.huff_map.get_huff_elem(char)
            code = huff_element.get_code()
            binary_string += code

        return binary_string

    def compress(self, file_str):
        """
        Compresses a passed in string of characters from a text file:
        1. take the passed in file_str and add EOF marker
        1. build the character frequency map of HuffElements
        2. build the Huffman Tree using the HuffPQ of HuffTrees
        3. build the Huffman codes, recursively traversing the tree
        4. build the Huffman encoded binary string and return it
        """
        EOF = chr(127)
        file_str += EOF
        self.build_huff_map(file_str)
        self.build_huff_tree()
        self.build_huff_codes(self.huff_tree.root)
        encoded_b_string = self.build_binary_str(file_str)

        return encoded_b_string

    def decompress(self, binary_str):
        """
        1. Get the root node of the Huffman tree and set a 
           current node pointing to the root node
        2. Loop through each character (0 or 1) in the binary_str:
           a. Traverse the Huffman tree starting from the root going
              left with '0' and right with '1' until you find a leaf 
              node
           b. When you find a leaf node (both left and right node
              pointers are None), retrieve the file string character 
              from the HuffNode 
           c. Check the character for the EOF char 
              and break when found
           d. Reset the current node pointer to root
        3. Return the decompressed string
        """
        decoded_str = ""
        EOF = chr(127)

        root_node = self.huff_tree.root
        current_node = root_node

        for char in binary_str:
            if char == '0':
                current_node = current_node.left
            elif char == '1':
                current_node = current_node.right

            if current_node.right is None and current_node.left is None:
                char = current_node.get_char()
                if char == EOF:
                    break

                decoded_str += char
                root_node = self.huff_tree.root
                current_node = root_node
        print(decoded_str)

        return decoded_str
