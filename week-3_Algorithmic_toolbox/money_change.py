def main():
    money = int(input())
    denoms = [10, 5, 1]
    print(money_change_recursive(money, denoms))

def money_change_recursive(money, denoms):
    if money == 0:
        return 0
    max_coin = max(denoms)
    if max_coin > money:
        denoms.remove(max_coin)
        return money_change_recursive(money, denoms)
    else:
        return 1 + money_change_recursive(money - max_coin, denoms)


if __name__ == '__main__':
    main()