import sys
def main():
    # d --> full distance
    # m --> max miles with full tank
    # n --> number of stops to refill.
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, input().split()))
    location = 0
    res = refill(location, stops, d, m)
    if res == -1:
        print('-1')
    else:
        print(res)

def refill(location, stops, d, m):
    if location + m >= d:
        return 0
    if not stops or (stops[0] - location) > m:
        print(int('-1'))
        sys.exit()
    last = location
    while stops and (stops[0] - location) <= m:
        last = stops[0]
        stops.remove(stops[0])
    return 1 + refill(last, stops, d, m)


if __name__ == '__main__':
    main()