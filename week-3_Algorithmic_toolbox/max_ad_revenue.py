def main():
    
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = 0
    a.sort(reverse=True)
    b.sort(reverse=True)
    for i in range(n):
        res += a[i] * b[i]
    print(res)


if __name__ == '__main__':
    main()