Plus Minus

#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

negative_count = 0.0
pos_count = 0.0
zero_count = 0.0

for index in arr:
    if index < 0:
        negative_count += 1
    elif index == 0:
        zero_count += 1
    elif index > 0:
        pos_count += 1

print(pos_count / n)
print(negative_count / n)
print(zero_count / n)
