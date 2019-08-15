"""
 Filename: vig_huff_main.py
 Programmer: Alex Lopez Torres Riega
 Date: November 12, 2018

 Description:
    Project 3: Encryption/Compression Project

    Object-Oriented Program that encrypts a message, compresses
    the message, decompresses the message, and decrypts the message.

    Uses the Vigenere encryption/decryption algorithm to encrypt and
    decrypt a text file.

    Uses the Huffman Codes algorithm to compress and decompress a text file.

    Uses a Python Nested list, Heap (Priority Queue) and Tree.

"""

from huffman import Huffman
from vigenere import Vigenere

BITARRAY_EXISTS = True
try:    
    from bitarray import bitarray
except:    
    BITARRAY_EXISTS = False


def main():
    """
    """
    INPUT_FILE = "FDREconomics.txt"    
    DECRYPT_FILE = "FDREconomicsDecrypt.txt"
    ENCRYPT_FILE = "FDREconomicsEncrypt.txt"        
    COMPRESS_DAT_FILE = "FDREconomicsComp.dat"   
    ENCRYPT_COMPRESS_DAT_FILE = "FDREconomicsEncryptComp.dat"
    DECRYPT_COMPRESS_FILE = "FDREconomicsDecryptComp.txt"
    
    VIGENERE_KEY = "I love the USA!!"
    
    print("(1) Read in original file: Using " + INPUT_FILE)
    print("    Print the original file:")
    print()

    file_str = open(INPUT_FILE, 'r').read()
    print(file_str)
    print() 
    
    print("(2) Encrypt original file using key: '{}'".format(VIGENERE_KEY))
    print()

    vig = Vigenere(VIGENERE_KEY)
    en_file_str = vig.encrypt(file_str)

    print("(3) Write out the encrypted file without compression")
    print("    Encrypted original file: Using " + ENCRYPT_FILE)
    print()

    open(ENCRYPT_FILE, 'w').write(en_file_str)
    
    print("(4) Read in encrypted original file: " + ENCRYPT_FILE)
    print("    Decrypt encrypted file using key")
    print("    Print out decrypted file:")
    print()

    en_file_str = open(ENCRYPT_FILE, 'r').read()
    message = vig.decrypt(en_file_str)
    print(message)
    print()
    
    print("(5) Write out the decrypted file")
    print("    Decrypted file: Using " + DECRYPT_FILE)
    print()

    open(DECRYPT_FILE, 'w').write(message)

    print("(6) Compress the original file without encryption")
    print("    Write out the file compressed without encryption")
    print("    Compressed original file: Using " + COMPRESS_DAT_FILE)
    print()

    huff = Huffman()
    binary_str = huff.compress(file_str)

    if BITARRAY_EXISTS: 
        write_bin_file(COMPRESS_DAT_FILE, binary_str)     

    print("(7) Read in compressed original file without encryption")
    print("    Decompress compressed file")
    print("    Print out decompressed file")
    print()

    if BITARRAY_EXISTS: 
        binary_str = read_bin_file(COMPRESS_DAT_FILE) 
        
    message = huff.decompress(binary_str)
    print(message)
    print()
	
    print("(8) Encrypt original file using key")
    print()

    vig = Vigenere(VIGENERE_KEY)
    en_file_str = vig.encrypt(file_str)
    
    print("(9) Compress the encrypted file")
    print("    Write out the compressed encrypted file")
    print("    Compressed encrypted file: Using " + ENCRYPT_COMPRESS_DAT_FILE)
    print()

    huff = Huffman()
    binary_str = huff.compress(en_file_str)

    if BITARRAY_EXISTS: 
        write_bin_file(ENCRYPT_COMPRESS_DAT_FILE, binary_str)         

        
    print("(10) Decompress compressed encrypted file")
    print("     Read in compressed encrypted file")
    print("     Compressed encrypted file: Using " + ENCRYPT_COMPRESS_DAT_FILE)
    print()
    
    if BITARRAY_EXISTS: 
        binary_str = read_bin_file(ENCRYPT_COMPRESS_DAT_FILE)	
 
    message = huff.decompress(binary_str)

    print()
    print("(11) Decrypt decompressed file using key")
    print("     Print out decrypted decompressed file")
    print()

    file_str = vig.decrypt(message)
    print(file_str)
    print()
    
    print("(12) Write out the decrypted decompressed file")
    print("     Decrypted decompressed file: Using " + DECRYPT_COMPRESS_FILE)
    
    open(DECRYPT_COMPRESS_FILE, 'w').write(file_str)	


def write_bin_file(filename, binary_str):
    """
    This function writes a compressed (binary) file to the disk 
    """
    bits = bitarray(binary_str)
    out_file = open(filename, 'wb')
    bits.tofile(out_file)
    out_file.close()


def read_bin_file(filename):        
    """
    This function reads a compressed (binary) file to the disk 
    """
    bit_str = bitarray()
    input_file = open(filename, 'rb')
    bit_str.fromfile(input_file)
    input_file.close()
    
    # Need to turn bitarray into a string of 1's and 0's
    bin_str = ""
    for b in bit_str:
        if b:
            bin_str += "1"
        else:     
            bin_str += "0"
    return  bin_str

main()
