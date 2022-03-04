"""I_love_%username%"""
n = int(input())
score = list(map(int, input().split()))
count = 0
max_score = score[0]
min_score = score[0]
for i in score[1:]:
    if i > max_score:
        max_score = i
        count += 1
    if i < min_score:
        min_score = i
        count += 1
print(count)
