# solution for https://open.kattis.com/problems/collatz
# Collatz Conjecture
# Submission Accepted
#
# given 2 starting values, say after how many steps their Collatz sequences "meet" for the first time (the first
# number that occurs in both sequences) and at which number they meet.
#
# Sample Input:
# 7 8
# 27 30
# 0 0
#
# Sample Output:
# 7 needs 13 steps, 8 needs 0 steps, they meet at 8
# 27 needs 95 steps, 30 needs 2 steps, they meet at 46

import sys
from bisect import bisect_left


# use built-in python bisect module
def binary_search(li, it, lo=0, hi=None):    # can't use a to specify default for hi
    hi = hi if hi is not None else len(li)   # hi defaults to len(a)
    pos = bisect_left(li, it, lo, hi)           # find insertion position
    return pos if pos != hi and li[pos] == it else -1  # don't walk off the end


# Collatz for first integer
def collatz(x):
    steps_x.append(int(x))
    if x == 1:
        return
    if x % 2 == 0:
        return collatz(x/2)
    else:
        return collatz(3*x+1)


# Collatz for second integer - will stop once an intersection point has been found
def collatz_y(y):
    steps_y.append(int(y))
    if binary_search(steps_x_copy, int(y)) != -1:
        global search
        search = True
        return
    if y == 1:
        return
    if y % 2 == 0:
        return collatz_y(y/2)
    else:
        return collatz_y(3*y+1)


inp = sys.stdin.read()
i = inp.split("\n")

for item in i:
    line = item.split(" ")
    if line[0] != "":
        if line[0] and line[1] != "0":
            # variables
            steps_x = []
            steps_y = []
            search = False

            ix = int(line[0])  # integer x
            iy = int(line[1])  # integer y

            # do stuff
            collatz(ix)
            steps_x_copy = steps_x.copy()
            steps_x_copy.sort()
            collatz_y(iy)

            if search:
                steps_x_split = steps_x[:steps_x.index(steps_y[-1])]
                print(str(ix) + " needs " + str(len(steps_x_split)) + " steps, " + str(iy) + " needs "
                      + str((len(steps_y)-1)) + " steps, they meet at " + str(steps_y[-1]))
            else:
                print(str(ix) + " needs " + str(len(steps_x)-1) + " steps, " + str(iy) + " needs "
                      + str((len(steps_y)-1)) + " steps, they meet at " + str(steps_y[-1]))
