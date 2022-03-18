def main():
    n = int(input())
    sequence = map(int,input().split())
    result = max_pairwise_product(sequence)
    print(result)


def max_pairwise_product(sequence):
    sequence = sorted(sequence)
    result = sequence[-1] * sequence[-2]
    return result


if __name__ == '__main__':
    main()