# https://www.hackerrank.com/challenges/matrix-script/problem

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
message = [line[i] for i in range(m) for line in matrix]
message = ''.join(message)
pattern = r'([A-Za-z0-9])[!@#$%&\s]+(?=[A-Za-z0-9])'
message = re.sub(pattern,r'\1 ', message)
print(message)
