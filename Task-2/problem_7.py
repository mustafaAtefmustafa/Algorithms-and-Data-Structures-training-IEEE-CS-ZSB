"""Andryusha and Socks"""
n = int(input())
socks = list(map(int, input().split()))
socks_on_table = 0
y = []
for i in socks:
    if i in y:
        y.remove(y[-1])
    else:
        y.append(i)
        socks_on_table = len(y)
print(socks_on_table)
