"""One-dimensional Japanese Crossword"""
n = int(input())
word = input()
arr = []
count = 0
for i in range(n + 1):
    if i >= n:
        if word[i - 1] == "B":
            arr.append("B" * count)
            break
        else:
            break

    if word[i] == "B":
        count += 1
        continue
    else:
        if count != 0:
            arr.append("B" * count)
            count = 0
        else:
            continue

if len(arr) > 0:
    print(len(arr))
    for i in arr:
        print(len(i), end=" ")
else:
    print(0)
