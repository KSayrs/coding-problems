# Solution for https://open.kattis.com/problems/trik
# Trik
# Submission Accepted

import sys

positions = [1, 2, 3]


def swap(pos1, pos2):
    temp = positions[pos1]
    positions[pos1] = positions[pos2]
    positions[pos2] = temp


for i in sys.stdin:
    noot = list(i)
    for char in noot:
        if char == 'A':
            swap(0, 1)
        elif char == 'B':
            swap(1, 2)
        elif char == 'C':
            swap(0, 2)

print(positions.index(1) + 1)
