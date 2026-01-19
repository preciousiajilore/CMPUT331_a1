#!/usr/bin/python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2026 Precious Ajilore
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential 
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including 
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
#---------------------------------------------------------------

"""
CMPUT 331 Assignment 1 Student Solution
January 2026
Author: Precious Ajilore
"""


from sys import flags

LETTERS = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

def get_map(letters=LETTERS):
    #build two dictionaries
    #char_to_index: maps each letter to its index
    #index_to_char: maps each index to its letter
    #if letters = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' then A -> 0, B -> 1, ..., Z -> 24
    char_to_index = {}
    index_to_char = {}
    for i, char in enumerate(letters):
        char_to_index[char] = i
        index_to_char[i] = char
    return (char_to_index, index_to_char)


def encrypt(message: str, key: str, letters: str = LETTERS) -> str:
    """
    Docstring for encrypt
    should return the message string such that each letter has been caesar shifted by the key
    but the key changes to the previous plaintext letter for each letter encrypted
    :param message: Description
    :type message: str
    :param key: Description
    :type key: str
    :param letters: Description
    :type letters: str
    :return: Description
    :rtype: str
    """
    char_to_index, index_to_char = get_map(letters)
    current_key = key.upper()
    n = len(letters)
    #key amount
    message = message.upper()
    key = key.upper()

    if current_key not in letters:
        raise ValueError("Key must be a single letter in LETTERS")
    
    result = []
    for char in message:
        if char in letters:
            #do the shifting here
            m = char_to_index[char]
            k = char_to_index[current_key]
            c = (m + k) % n
            #get the encrypted character from index_to_char
            encrypted_char = index_to_char[c]
            #append to result string
            result.append(encrypted_char)
            current_key = char  # update the key to the current plaintext letter
        else:
            #non-letter characters are not changed
            result.append(char)
    result = ''.join(result)
    return result

def decrypt(message: str, key: str, letters: str = LETTERS):
    """
    Docstring for decrypt
    #reverse the shift performed in encrypt
    :param message: Description
    :type message: str
    :param key: Description
    :type key: str
    :param letters: Description
    :type letters: str
    """
    char_to_index, index_to_char = get_map(letters)
    n = len(letters)
    current_key = key.upper()

    if current_key not in letters:
        raise ValueError("Key must be a single letter in LETTERS")
    
    message = message.upper()
    result = []

    for char in message:
        if char in letters:
            m = char_to_index[char]
            k = char_to_index[current_key]
            c = (m - k) % n
            decrypted_char = index_to_char[c]
            result.append(decrypted_char)
            current_key = decrypted_char  # update the key to the current plaintext letter
        else:
            result.append(char)
    return ''.join(result)
     


def test():
    global SHIFTDICT, LETTERDICT 
    SHIFTDICT, LETTERDICT = get_map()
    #SHIFTDICT, LETTERDICT = get_map("ZYXWVUTSRQPONMLKIGFEDCBAH")
    #assert decrypt(encrypt("FOO", "G"), "G") == "FOO"
    encrypted = encrypt("THIS IS PROBLEM 2 OF ASSIGNMENT 1.", "X")
    print("Encrypted message:", encrypted)
    decrypted = decrypt(encrypted, "X")
    print("Decrypted message:", decrypted)

    msg = "THIS IS PROBLEM 2 OF ASSIGNMENT 1."
    key = "X"
    assert decrypt(encrypt(msg, key), key) == msg.upper()
    assert decrypt(encrypt("A!A", "B"), "B") == "A!A"
   


if __name__ == "__main__" and not flags.interactive:
    test()