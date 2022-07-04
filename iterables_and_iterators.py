# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

import itertools

N = int(input())
letters = input().split()
K = int(input())

a_count = 0
combs = list(itertools.combinations(letters,K))
for i in combs:
    if 'a' in i:
        a_count += 1

print(round(a_count / len(list(combs)), 3))
