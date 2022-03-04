"""Stones on the Table"""
n = int(input())
stones = input()
i = 0
j = 1
count = 0
for i in range(n):
    if j >= n:
        break
    if stones[i] == stones[j]:
        count += 1
        j += 1
        continue
    else:
        j += 1
print(count)
