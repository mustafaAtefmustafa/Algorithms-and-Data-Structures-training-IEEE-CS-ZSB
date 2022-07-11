PISANO_LENGTH = 60


def main():
    n = int(input())
    print(eff_algo_fib((n + 2) % PISANO_LENGTH))


def eff_algo_fib(n):
    if n == 0:
        return 0
    arr = [0 , 1]
    for i in range(n - 1):
        arr.append(arr[-1] + arr[-2])
        
    return (arr[-1] - 1) % 10


if __name__ == '__main__':
    main()