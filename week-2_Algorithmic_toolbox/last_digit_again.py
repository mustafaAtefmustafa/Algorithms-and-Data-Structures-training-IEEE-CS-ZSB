## f(n + 2)%10 - f(m + 1) % 10
PISANO_LENGTH = 60

def main():
    m, n = map(int, input().split())
    m = m + 1
    n = n + 2
    first = eff_algo_fib(n % PISANO_LENGTH)
    second = eff_algo_fib(m % PISANO_LENGTH)
    print ((first - second) % 10)
    
def eff_algo_fib(i):
    if i == 0:
        return 0
    arr = [0 , 1]
    for i in range(i - 1):
        arr.append(arr[-1] + arr[-2])
    return arr[-1] % 10

if __name__ == '__main__':
    main()