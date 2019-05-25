# Kattis problem https://open.kattis.com/problems/aaah
# Aaah!
# Submission accepted

import sys

thein = sys.stdin.read()
ins = thein.split("\n")

if len(ins[0]) >= len(ins[1]):
    print("go")
else: print("no")
