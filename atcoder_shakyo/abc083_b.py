# https://atcoder.jp/contests/abc083/tasks/abc083_b

n, a, b = (int(x) for x in input().split())
c = 0
sum = 0

for i in range(1, n + 1):
    c += 1
    if a <= c <= b:
        sum += i
    while i%10 == 9:
        c -= 9
        i //= 10

print(sum)