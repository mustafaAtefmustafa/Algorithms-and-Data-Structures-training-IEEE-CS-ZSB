"""Shaass and Oskols"""
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if x - 1 >= 0:
        arr[x - 1] += y
    if x + 1 < len(arr):
        arr[x + 1] += arr[x] - y - 1
    arr[x] = 0
for k in arr:
    print(k)
