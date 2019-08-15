"""
Background to Using the Vigenere Square for Encryption

The rows are associated with the characters in the key and the columns 
are associated with the characters in the message to encrypt.  The key 
will be used over and over again matching the letters in the message 
with the letters in the key. 

Encryption: Find the ciphertext character in the Vigenere square 
matrix by the following steps:
a) Using the character from the key, find the row where it exists by 
   looking down column 0 until you find the correct row.
b) Using the character from the plaintext message, find column where 
   it exists by looking across row 0 until you find the correct column.
c) The ciphertext character will be the one in the in the matrix 
   having the row and column found above.
d) Add the ciphertext letter to the coded message.

Decryption: Find the plaintext character in the Vigenere square 
matrix by the following steps:
a) Find the ciphertext letter in the Vigenere square, using the key 
   letter row.
b) In that same column, get the character at row 0, this is the 
   plaintext letter.
c) Add the plaintext letter to the decoded message.
"""


class Vigenere:    
    def __init__(self,key):
        """
        Create Vigenere object: initialize key and matrix
        """
        self._key = key
        self._vig_squ = self.create_vig_square()

    def create_vig_square(self):
        """
        Create the vigenere square, using 128 rows and 128 columns
        Use a nested list for the matrix and a nested loop to create 
           each inner row and add it to the outer matrix.
        Each element of the inner row is one more in ASCII code value 
           than the previous element.  After getting to 128, you must
           go back to 0.
        """
        vig_square = []

        for row in range(128):
            vig_row = []
            chr_code = row
            for col in range(128):
                # Changes chr_code back to 0 if it surpasses last character.
                if chr_code == 128:
                    chr_code = 0
                char = chr(chr_code)
                vig_row.append(char)
                chr_code = chr_code + 1
            vig_square.append(vig_row)

        return vig_square
            
    def encrypt(self, msg):
        """
        Traverse the message getting each letter 
           and finding its encoding:
        Get the row index of the key char using get_row_index
        Get the column index of the message char using get_col_index
        Use the row and column indices to find the code character
           in the Vigenere square
        Add code character to encoded message    
        """
        coded_msg = ""
        key_index = 0
        for char in range(len(msg)):
            msg_character = msg[char]
            key_letter = self._key[key_index]
            key_index += 1
            row = self.get_row_index(key_letter)
            col = self.get_col_index(msg_character)
            coded_msg += (self._vig_squ[row][col])

            # Go back to the beginning of the key.
            if key_index >= len(self._key):
                key_index = 0

        return coded_msg

    def decrypt(self, coded_msg):
        """
        Traverse the code getting each letter 
           and finding its decoding:
        Get the message character using get_plain_text_char 
        Add message character to decoded message   
        """
        decoded_msg = ""
        key_index = 0
        for char in range(len(coded_msg)):
            msg_character = coded_msg[char]

            key_letter = self._key[key_index]
            key_index += 1
            decoded_msg += self.get_plain_text_char(msg_character, key_letter)

            # Go back to first letter of the key.
            if key_index >= len(self._key):
                key_index = 0

        return decoded_msg

    def get_col_index(self, char):
        """
        The first row of the Vigenere square is vig_squ[0].
        This is used to match chars from the message to encrypt.
        Return the column index in row 0 containing the char
        """
        col_index = 0
        for i in range(128):
            if char == self._vig_squ[0][i]:
                col_index = i
        return col_index

    def get_row_index(self, key_char):
        """
        The first column of the Vigenere square is vig_squ[][0]
        This is used to match chars from the key.
        Return the row index in col 0 containing the key char
        """
        row_index = 0
        for i in range(128):
            if key_char == self._vig_squ[i][0]:
                row_index = i
        return row_index

    def get_plain_text_char(self, coded_char, key_char):
        """
        Use the row index of the key char and the column index of
        the coded message char in that row to locate the column in
        row 0 of the plaintext char and return that element value.
        """
        plain_text_char = ''
        cipher_row = self.get_row_index(key_char)

        # Iterate through row to right column after finding row for the key letter
        for col in range(128):
            # If the location (row,col) of the coded character is on the same row and column as the key,
            # we use that column to find the plaintext letter in row 0.
            if coded_char == self._vig_squ[cipher_row][col]:
                plain_text_char = self._vig_squ[0][col]
        return plain_text_char
