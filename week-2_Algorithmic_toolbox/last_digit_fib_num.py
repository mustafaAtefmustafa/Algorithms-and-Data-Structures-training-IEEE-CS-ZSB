def main():
    print(eff_algo_fib(int(input())))


def eff_algo_fib(n):
    if  n == 0:
        return 0
    arr = [0 , 1]
    for i in range(n - 1):
        arr.append((arr[-1] + arr[-2]) % 10) 
    return arr[-1]

if __name__ == '__main__':
    main()