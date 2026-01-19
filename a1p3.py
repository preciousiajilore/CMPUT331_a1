#!/usr/bin/python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2026 <<Insert your name here>>
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
Author: <Your name here>
"""


from sys import flags
from a1p1 import encrypt, decrypt

LETTERS = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'


def crack_caesar(ciphertext, val_words):
    
    #for ech letter in LETTERS: candidate plaintext = decrypt(ciphertext, letter)
    #count how many words in candidate plaintext are in val_words
    #keep track of the candidate plaintext with the highest count of valid words
    best_count = 0
    best_plaintext = None
    best_key = None
    for letter in LETTERS:
        possible_plaintext = decrypt(ciphertext, letter)
        words = possible_plaintext.split()
        count = 0
        for token in words:
            if token in val_words:
                count += 1
        if count > best_count or (count == best_count and (best_plaintext is None or possible_plaintext < best_plaintext)):
            best_count = count
            best_plaintext = possible_plaintext
            best_key = letter
    return (best_plaintext, best_key)


def form_dictionary(text_address='carroll-alice.txt'):
    with open(text_address, 'r') as f:
        text = f.read()
    text = text.upper()
    #remove punctuation 
    for char in text:
        if char not in LETTERS and char != ' ' and char != '\n':
            text = text.replace(char, '')
    words = text.split()
    word_set = set(words)
    return word_set



def test():
    #testing dictionary formation
    dictionary = form_dictionary()
    #print("word in dictionary:", list(dictionary)[0])
    #assert 'ALICE' in dictionary
    #assert 'WONDERLAND' in dictionary
    #assert 'XYZ' not in dictionary
    assert crack_caesar('TBHZLIB QL TLKABOHXKA', form_dictionary()) == ('WELCOME TO WONDERLAND', 'X')
    print(crack_caesar("TBHZLIB QL TLKABOHXKA", form_dictionary()))

if __name__ == "__main__" and not flags.interactive:
    test()