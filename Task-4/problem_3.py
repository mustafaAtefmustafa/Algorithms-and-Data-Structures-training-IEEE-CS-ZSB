"""BerOS file system"""


def main():
    path = input()
    path = '/'+'/'.join(i for i in path.split("/") if i)
    print(path)


if __name__ == '__main__':
    main()
