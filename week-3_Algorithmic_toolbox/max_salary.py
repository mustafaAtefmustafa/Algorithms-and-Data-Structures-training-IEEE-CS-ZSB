def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    largest_concat = largest_concat_iter(numbers.copy())
    print(largest_concat)

def largest_concat_iter(numbers):
    number = ""
    while numbers:
        max_number = max(numbers)
        for digit in numbers:
            if is_greater_or_equal(digit,max_number):
                max_number = digit
        number += str(max_number)
        numbers.remove(max_number)
    return number

def is_greater_or_equal(digit, max_digit):
    if int(str(digit) + str(max_digit)) >= int(str(max_digit) + str(digit)):
        return True
    else:
        return False


if __name__ == '__main__':
    main()