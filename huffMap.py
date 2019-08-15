from map import Map
from huffElement import HuffElement


class HuffMap(Map): 
    """
    This class inherits from Map with methods tailored
    to Huffman encoding
    """
    def __init__(self):
        """
        Create the HuffMap object by calling
        the parent constructor
        """
        super().__init__()

    def contains_char(self, ch):
        """
        Checks for previous existence of character in HuffMap
        Returns True, when found, otherwise returns False
        """
        return self._find_position(ch) is not None

    def add_char(self, char):
        """
        Add a new character to the HuffMap
        """
        element = HuffElement(char)
        self.add(char, element)

    def get_huff_elem(self, char):
        """
        Returns the HuffElement for a passed in character
        """
        return self.get_value(char)

    def get_char_set(self):
        """
        Returns the set of characters in the HuffMap
        """
        return self.get_key_set()

