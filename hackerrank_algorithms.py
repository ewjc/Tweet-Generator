ALGORITHMS

(FROM WARMUP)
1. PLUS MINUS - 98.10%
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

--------------------------------------------------------------
(FROM IMPLEMENTATION)
2. ANGRY PROFESSOR - 94.62%

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))

    students_ontime = 0

    for time in a:
        if time <= 0:
            students_ontime += 1

    if students_ontime >= k:
        print('NO')
    else:
        print('YES')
--------------------------------------------------------------
(FROM IMPLEMENTATION)
3. BETWEEN TWO SETS - 87.43%

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))

total_x = 0

for number in a:
    stored_number_a = number
    if stored_number_a < number:
        stored_number_a == number

for number in set(b):
    stored_number_x = number
    if stored_number_x / stored_number_a:
        total_x += 1

print(total_x)
