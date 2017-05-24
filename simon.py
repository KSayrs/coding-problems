# Solution for https://open.kattis.com/problems/simonsays
# Simon Says
# submission accepted

import sys

thein = sys.stdin.read()
ins = thein.split("\n")
lines = ins[1:-1]

simon = []
for line in lines:
    if line.startswith("Simon says"):
        simon.append(line[10:])

for command in simon:
    print(command)
