# 3D printed statues
# https://open.kattis.com/problems/3dprinter
# Submission accepted

import sys
import math

number = int(sys.stdin.readline())

print(math.ceil(math.log2(number)) +1)
