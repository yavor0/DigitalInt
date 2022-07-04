# https://www.hackerrank.com/challenges/word-order/problem

n = int(input())
words = []
for i in range(n):
    words.append(input())

occurrences = {}
for word in words:
    if word in occurrences:
        occurrences[word]+=1
    else:
        occurrences[word]=1

print(len(occurrences))
for i in occurrences:
    print(occurrences[i], end=" ")
