# Solution for https://open.kattis.com/problems/flexible
# Flexible Spaces
# Submission: accepted

'''
Sample Input 1
10 3
1 4 8

Sample Output 1
1 2 3 4 6 7 8 9 10

Sample Input 2
6 2
2 5

Sample Output 2
1 2 3 4 5 6

'''

import sys

thein = sys.stdin.read()
i = thein.split("\n")

line1 = i[0].split(" ")  # W of room P number of partitions
line2 = i[1].split(" ")  # (optional) locations of the P partitions

roomSize = int(line1[0])

widths = [roomSize]

for part in line2:
    widths.append(int(part))
    if roomSize-int(part) != 0:
        widths.append(roomSize-int(part))
    for item in reversed(line2):
        if item != line2[0] and int(part)-int(item) != 0:
            widths.append(abs(int(part)-int(item)))

noot = list(set(widths))

noot.sort()

for n in noot:
    print(str(n) + " ", end="", flush=True)
