"""Pages"""


def main():
    n, p, k = map(int, input().split())
    if p - k > 1:
        print("<<", end=" ")
    for i in range(p-k, p+k+1):
        if i in range(1, n+1):
            if i == p:
                print(f"({i})", end=" ")
            else:
                print(i, end=" ")
    if p + k < n:
        print(">>")


if __name__ == '__main__':
    main()
