while True:
    n = int(input())
    if n <= 2000 and n >= 0:
        break
score = 0
if n <= 800:
    score = 1
    print(score)
elif n <= 1400:
    score = 2
    print(score)
else:
    score = 3
    print(score)
