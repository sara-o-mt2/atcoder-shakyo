# https://atcoder.jp/contests/abc083/tasks/abc083_b

n, a, b = map(int,input().split());c=0
while n:c+=n*(a<=sum(map(int,str(n)))<=b);n-=1
print(c)