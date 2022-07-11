"""Calculating Least Common Multiple using lcm = ab / gcd(a,b)"""

def main():
    a, b = map(int,input().split())
    print(int(a*b / eculidean_gcd(a, b)))

def eculidean_gcd(a, b):
    """Efficient way to calculate GCD"""

    if b == 0:
        return a
    else:
        a = a % b
        return eculidean_gcd(b, a)



if __name__ == '__main__':
    main()