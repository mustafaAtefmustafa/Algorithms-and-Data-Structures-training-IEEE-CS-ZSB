"""Brain's Photos"""
import sys
n, m = map(int, input().split())
colors = [input().split() for i in range(n)]
for i in range(n):
    for j in range(m):
        if colors[i][j] in ['C', 'Y', 'M']:
            print("#Color")
            sys.exit()
    else:
        print("#Black&White")
        sys.exit()
        
