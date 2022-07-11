def main():
    a, b = input().split()
    print(eculidean_gcd(int(a), int(b)))

def eculidean_gcd(a, b):
    """Efficient way to calculate GCD"""

    if b == 0:
        return a
    else:
        a = a % b
        return eculidean_gcd(b, a)



if __name__ == '__main__':
    main()