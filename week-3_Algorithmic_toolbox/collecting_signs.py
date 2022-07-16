def main():
    n = int(input())
    segs = []
    for i in range(n):
        x,y = map(int,input().split())
        segs.append([x, y])
    segs.sort(key = lambda i: i[1])
    res = []
    i = 0
    while i < n:
        right = segs[i][1]
        sign_time = right
        i += 1
        while i < n and segs[i][0] <= right:
            if segs[i][1] < sign_time:
                sign_time =segs[i][1]
            i += 1
        res.append(sign_time)
    
    print(len(res))
    for k in res:
        print(k, end=" ")


if __name__ == '__main__':
    main()