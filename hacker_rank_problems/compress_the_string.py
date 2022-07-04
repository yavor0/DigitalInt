# https://www.hackerrank.com/challenges/compress-the-string/problem

import itertools

inp = input()
# inp = '1222311'
key_func = lambda x: x

for key, group in itertools.groupby(inp, key_func):
    ans_tup = len(list(group)), int(key)
    print(ans_tup, end=' ')

