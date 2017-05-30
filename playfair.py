# https://open.kattis.com/problems/itsasecret
# Submission not accepted - runtime too long on case 2 (>1s)

from sys import stdin

alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # alphabet excluding j


def generate_cipher(phrase):
    up = phrase.upper()
    up = "".join(up.split(" "))
    up = up.replace("J", "I")
    up += alphabet
    s = sorted(set(up), key=up.index)
    s = "".join(s)
    long = list(s)
    group2 = lambda flat, size: [flat[i:i + size] for i in range(0, 25, size)]
    make = group2(long, 5)
    # cipher = [s[j:j+5] for j in range(0, 25, 5)]
    # cipher = [[s[j] for j in range(0, 5)] for k in range(0, 25, 5)]
    return make


def findpos(matrix, letter):
    x = 0
    y = 0
    for n in range(5):
        for m in range(5):
            if matrix[n][m] == letter:
                x = n
                y = m
                return x, y
    return x, y


# ############## ENCRYPT ############################
def enc(phrase, cipher):
    dg = make_digraph(phrase)
    enc = []  # final encrypt
    for pair in dg:
        if pair == "XX":  # replace xx with yy and move on
            enc.append("YY")
        else:
            p1, q1 = findpos(cipher, pair[0])
            p2, q2 = findpos(cipher, pair[1])
            if p1 == p2:
                if q1 == 4:
                    q1 = -1
                if q2 == 4:
                    q2 = -1
                enc.append(cipher[p1][q1 + 1])
                enc.append(cipher[p2][q2 + 1])
            elif q1 == q2:
                if p1 == 4:
                    p1 = -1
                if p2 == 4:
                    p2 = -1
                enc.append(cipher[p1 + 1][q1])
                enc.append(cipher[p2 + 1][q2])
            else:
                enc.append(cipher[p1][q2])
                enc.append(cipher[p2][q1])
    return enc


# ###################### MAKE DIGRAPH #########################
def make_digraph(phrase):
    phrase = phrase.upper()
    phrase = "".join(phrase.split(" "))
    phrase = phrase.replace('J', "I")

    digraph = [phrase[x:x + 2] for x in range(0, len(phrase), 2)]

    rejoin = False
    for n in digraph:
        ind = digraph.index(n)
        try:
            if n[0] == n[1]:
                digraph[ind] = n[0] + "X" + n[1]
                rejoin = True
        except IndexError:
            digraph[ind] = n[0] + "X"

    if rejoin:
        digraph = "".join(digraph)
        return make_digraph(digraph)  # recursively recheck string

    else:
        return digraph


# ######### MAIN ##########

setlength = int(stdin.readline().strip()[:1])
while setlength != 0:
    key = stdin.readline().strip()
    c = generate_cipher(key)  # generate the cipher

    for i in range(setlength):
        line = stdin.readline().strip()
        encrypted = enc(line, c)
        newt = "".join(encrypted)
        print(newt)

        if i+1 == setlength:
            setlength = int(stdin.readline().strip()[:1])
            if setlength != 0:
                print()
