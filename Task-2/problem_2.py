"""Nastya and an Array"""


def main():
    n = int(input())
    arr = set(list(map(int, input().split())))
    count = 0
    for i in arr:
        if i != 0:
            count += 1
    print(count)


if __name__ == '__main__':
    main()
