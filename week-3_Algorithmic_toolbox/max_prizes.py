def main():
    n = int(input())
    l = []
    i = 0
    while n != 0:
        i += 1
        l.append(i)
        n -= i
        if n <= l[-1] and n != 0:
            n += i
            l.remove(i)
            l.append(n)
            break


    print(len(l))
    for j in l:
        print(j, end=" ")

if __name__ == '__main__':
    main()