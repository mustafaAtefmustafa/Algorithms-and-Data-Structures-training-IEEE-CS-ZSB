"""Counting Sticks"""
import sys


def main():
    expression = input()
    lhs = expression.find("+")
    rhs = len(expression) - expression.find("=") - 1
    mid = expression.find("=") - expression.find("+") - 1
    if lhs + mid == rhs:
        print(expression)
        sys.exit()
    else:
        if lhs + mid == rhs + 2:   # Then a stick was moved from lhs to rhs
            if lhs > 1:
                expression = expression[1:] + "|"
                print(expression)
            else:
                mid -= 1
                print("|"*lhs + "+" + "|"*mid + "=" + "|"*(rhs + 1))
        elif lhs + mid == rhs - 2:   # Then a stick was moved from rhs to lhs
            rhs -= 1
            mid += 1
            print("|"*lhs + "+" + "|"*mid + "=" + "|"*rhs)
        else:   # Nothing moved and Impossible to achieve
            print("Impossible")


if __name__ == '__main__':
    main()
