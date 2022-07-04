# https://www.hackerrank.com/challenges/ginorts/problem

letters, uppers, odds, evens = [],[],[],[]
for char in sorted(input()):
    if char.isalpha():
        x = uppers if char.isupper() else letters
    else:
        x = odds if int(char) % 2 else evens
    x.append(char)
print("".join(letters+uppers+odds+evens))
