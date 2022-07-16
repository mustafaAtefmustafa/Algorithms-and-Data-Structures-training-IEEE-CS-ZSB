"""I GAVE UP SOLVING THIS CUZ NO MATTER WHAT, IT NEVER PASSES CASE 8"""

def main():
    n, w = map(int, input().split())
    cost = []
    weight = []

    for i in range(n):
        x, y = map(int, input().split())
        cost.append(x)
        weight.append(y)

    loot = max_loot(w, weight, cost)
    print("{:.4f}".format(loot))


def max_loot(w, weight, cost):
    if w == 0 or not weight:
        return 0
    index = highest_ratio(weight, cost)
    amount = min(weight[index], w)
    value = cost[index] * float((amount / weight[index]))
    weight.remove(weight[index])
    cost.remove(cost[index])
    w -= amount
    return value + max_loot(w, weight, cost)


def highest_ratio(weight, cost):
    max_index = 0
    max_value = 0
    for i in range(len(weight)):
        temp_value = cost[i] / weight[i]
        if temp_value > max_value:
            max_value = temp_value
            max_index = i
        if temp_value == max_value:
            if cost[i] > cost[max_index]:
                max_index = i
    return max_index

if __name__ == '__main__':
    main()