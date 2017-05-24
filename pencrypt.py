# Solution for https://open.kattis.com/problems/permutationencryption
# Permutation Encryption
# Submission accepted

"""
Sample Input:

1 1
Four score and seven years ago
2 2 1
our fathers brough forth on this continent a new nation,
5 1 3 2 5 4
conceived in liberty and dedicated to the proposition
10 5 10 8 1 3 6 4 7 2 9
that all men are created equal.
0

Sample Output:

'Four score and seven years ago'
'uo rafhtre srbuohgf rohto  nhtsic noitentna n wen taoi,n'
'cnoeciev di nilbreyt na dddeciaet dt ohtep orpsotiino  '
' mltaatlh rece ea nr luaeedqta   .      '

"""

import sys


def swap(keys, splittext):
    encryptsmall = []
    newsplit = []
    for char in splittext:
        newsplit.append(char)

    if len(newsplit) < len(keys):
        for space in range(len(newsplit), len(keys)):
            newsplit.append(" ")

    for z in range(len(keys)):
        val = int(keys[z])
        encryptsmall.append(newsplit[val-1])

    return encryptsmall

thein = sys.stdin.read()
i = thein.split("\n")

keys = i[:-1:2]  # list of all the keys
text = i[1:-1:2]  # list of all the messages
amount = len(text)

for item in range(amount):
    encrypted = []
    line = text[item]  # individual message
    keynum = keys[item].split(" ")
    keynum = keynum[1:]

    n = len(keynum)
    splitText = [line[i:i+n] for i in range(0, len(line), n)]

    for sets in range(len(splitText)):
        tiny = swap(keynum, splitText[sets])
        newtiny = "".join(tiny)
        encrypted.append(newtiny)

    encrypted = "".join(encrypted)
    neone = "'" + str(encrypted) + "'"
    print(neone)
