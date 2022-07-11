def main():
    n, m = map(int,input().split())
    pisano_length = pisano_period(m)
    result = eff_algo_fib(n % pisano_length, m) 
    print(result)


def eff_algo_fib(n, m):
    if n == 0:
        return 0
    arr = [0 , 1]
    for i in range(n - 1):
        arr.append(arr[-1] + arr[-2])
    return arr[-1] % m


def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m 
      
        # A Pisano Period starts with 01 
        if (previous == 0 and current == 1): 
            return i + 1
            
if __name__ == '__main__':
    main()