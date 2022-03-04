"""Mishka and Contest"""
n, k = map(int, input().split())
problems = list(map(int, input().split()))
count = 0
while len(problems) > 0:
    if problems[0] <= k:
        count += 1
        problems.remove(problems[0])
    elif problems[-1] <= k:
        count += 1
        problems.pop()
        
    else:
        break
print(count)
