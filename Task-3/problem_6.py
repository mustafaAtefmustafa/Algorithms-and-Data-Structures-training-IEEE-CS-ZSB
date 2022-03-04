"""Coder"""

n = int(input())
if n % 2 == 0:
    print(int(n * n / 2))
else:
    print(int((n * n + 1) / 2))
arr = ["C", "."] * n
for i in range(n):
    if i % 2 == 0:
        print(*arr[:n], sep="")
    else:
        print(*arr[1:n + 1], sep="")
# c.c. -->0
# .c.c -->1
# c.c. -->2
# .c.c -->3
