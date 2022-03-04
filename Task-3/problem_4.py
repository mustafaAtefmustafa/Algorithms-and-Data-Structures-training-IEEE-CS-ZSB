"""Colorful Stones (Simplified Edition)"""
s = input()
t = input()
i = 0
for j in t:
    if j == s[i]:
        i += 1
    else:
        continue
print(i+1)
