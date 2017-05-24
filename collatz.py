# solution for https://open.kattis.com/problems/collatz
# Collatz Conjecture
# Submission Accepted

import sys
from bisect import bisect_left

stepsx = []
stepsy = []


def binary_search(a, x, lo=0, hi=None):    # can't use a to specify default for hi
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)
    pos = bisect_left(a, x, lo, hi)           # find insertion position
    return pos if pos != hi and a[pos] == x else -1  # don't walk off the end


def collatz(x):
    steps.append(int(x))
    if x == 1:
        return
    global count
    count += 1
    if x % 2 == 0:
        return collatz(x/2)
    else:
        return collatz(3*x+1)


def collatzy(y):
    steps.append(int(y))
    if binary_search(stepsxcopy, int(y)) != -1:
        global search
        search = True
        # print(search)
        return
    if y == 1:
        return
    global count
    count += 1
    if y % 2 == 0:
        return collatzy(y/2)
    else:
        return collatzy(3*y+1)


thein = sys.stdin.read()
i = thein.split("\n")

for item in i:
    line = item.split(" ")
    if line[0] != "":
        if line[0] and line[1] != "0":
            steps = []
            count = 0
            x = int(line[0])
            y = int(line[1])
            collatz(x)
            stepsx = steps
            stepsxcopy = stepsx.copy()
            stepsxcopy.sort()
            steps = []
            count = 0
            search = False
            collatzy(y)
            stepsy = steps

            if search:
                stepsxsplit = stepsx[:stepsx.index(stepsy[-1])]
                print(str(x) + " needs " + str(len(stepsxsplit)) + " steps, " + str(y) + " needs " + str((len(stepsy)-1)) + " steps, they meet at " + str(stepsy[-1]))
            else:
                print(str(x) + " needs " + str(len(stepsx)-1) + " steps, " + str(y) + " needs " + str(
                    (len(stepsy) - 1)) + " steps, they meet at " + str(stepsy[-1]))
