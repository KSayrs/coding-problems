# Solution for https://open.kattis.com/problems/permutationencryption
# Permutation Encryption
# Submission accepted
#
# The first line starts with an integer 1≤n≤201≤n≤20, the length of the key,
# followed by nn integers which form the permutation.
# The second line contains the message content to be encrypted. Input ends when nn is zero.
# This program encrypts everything on the second line, enclosed in single quotes.
#
# Sample Input:
#
# 1 1
# Four score and seven years ago
# 2 2 1
# our fathers brough forth on this continent a new nation,
# 5 1 3 2 5 4
# conceived in liberty and dedicated to the proposition
# 10 5 10 8 1 3 6 4 7 2 9
# that all men are created equal.
# 0
#
# Sample Output:
#
# 'Four score and seven years ago'
# 'uo rafhtre srbuohgf rohto  nhtsic noitentna n wen taoi,n'
# 'cnoeciev di nilbreyt na dddeciaet dt ohtep orpsotiino  '
# ' mltaatlh rece ea nr luaeedqta   .      '

import sys


def swap(key_list, chars):
    encrypt_small = []
    new_split = []
    for char in chars:
        new_split.append(char)

    if len(new_split) < len(key_list):  # fill string with filler spaces
        for space in range(len(new_split), len(key_list)):
            new_split.append(" ")

    for z in range(len(key_list)):
        val = int(key_list[z])
        encrypt_small.append(new_split[val-1])  # swap the characters

    return encrypt_small

inp = sys.stdin.read()
start = inp.split("\n")

keys = start[:-1:2]   # list of all the keys
text = start[1:-1:2]  # list of all the messages
amount = len(text)

for item in range(amount):
    encrypted = []
    line = text[item]  # individual message
    key_numbers = keys[item].split(" ")
    key_numbers = key_numbers[1:]

    # split text into character groupings of the length of the keys
    n = len(key_numbers)
    split_text = [line[i:i+n] for i in range(0, len(line), n)]

    for sets in range(len(split_text)):
        tiny = swap(key_numbers, split_text[sets])
        tiny = "".join(tiny)
        encrypted.append(tiny)

    encrypted = "".join(encrypted)
    encrypted = "'" + str(encrypted) + "'"
    print(encrypted)
