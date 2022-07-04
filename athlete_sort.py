# https://www.hackerrank.com/challenges/python-sort-sort/problem

n, m = map(int, input().split())
athletes = [list(map(int, input().split())) for i in range(n)]
k = int(input())

athletes = sorted(
    athletes,
    key=lambda t: t[k]
)

for athlete in athletes:
    for attr in athlete:
        print(attr, end=' ')
    print()

