from comparable import Comparable
from huffElement import HuffElement


class HuffNode(Comparable):
    """
    This class represents a node in a HuffTree, 
    where the node data is a HuffElement object
    The public instance variables are:
       - element: the HuffElement object
       - left: the root node of the left subtree off this node
       - right: the root node of the right subtree off this node
    """
    def __init__(self, element):
        """
        Constructor: Create HuffNode object
         - initialize data with passed in HuffElement
         - initialize nodes to None
        """
        self.element = element
        self.right = None
        self.left = None
 
    def get_char(self):
        """
        Return the character from the HuffElement
        """
        return self.element.get_char()

    def get_freq(self):
        """
        Return the character count from the HuffElement
        """
        return self.element.get_freq()

    def set_freq(self, count):
        """
        Set the character count in the HuffElement
        """
        self.element.set_freq(count)

    def get_code(self):
        """
        Return the Huffman code from the HuffElement
        """
        return self.element.get_code()

    def set_code(self, code):
        """
        Set the character count in the HuffElement
        """
        self.element.set_code(code)

    def compare(self, other_node):
        """
        Use the character frequency count for comparison,
        by calling the HuffElement compare method 
        """
        return self.element.compare(other_node)

    def __str__(self):
        """
        Return the string representation of the HuffElement
        """
        return str(self.element)
        

class HuffTree(Comparable):
    """
    This class represents a Huffman Encoding Tree
    There are two types of HuffTrees that are built
      1. the leaf nodes: built with the HuffElements
      2. the internal nodes: built with two HuffTrees
    """

    def __init__(self, element = None, left_tree = None, right_tree = None):
        """
        Constructor:
        The constructor parameters have default values.
        The constructor must be called using these keyword arguments:
        1. when building the internal nodes for the Huffman Tree, the
           element parameter is None 
        2. when building the leaf nodes the left and right subtree 
           root nodes will be None
        Initialize the root HuffNode instance variable appropriately  
        a) for the leaf Node, root is initialized with a HuffNode 
           using the element parameter
        b) for the internal Node, root is initialized with a 
           HuffNode using a HuffElement where the character is EOF 
        """
        EOF = chr(127)
        if left_tree is not None:
            # top of tree
            self.root = HuffNode(HuffElement(EOF))
            self.root.left = left_tree.root
            self.root.right = right_tree.root
            self.root.set_freq(left_tree.root.get_freq()+
                               right_tree.root.get_freq())
        else:
            self.root = HuffNode(element)

    def get_root(self):
        """
        Returns the root of the tree
        """
        return self.root

    def compare(self, other_huff_tree):
        """
        Compare the root node of this HuffTree 
        to that of the other HuffTree
        """
        if self.root.compare(other_huff_tree.get_root()) < 0:
            return -1
        if self.root.compare(other_huff_tree.get_root()) > 0:
            return 1
        else:
            return 0

