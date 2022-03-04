"""Bus to Udayland"""
def print_seats(seats):
    for i in range(len(seats)):
        for j in range(5):
            print(seats[i][j],end="")
        print()

n = int(input())
seats = []
free = 'O'
occupied = 'X'
for i in range(n):
    seats.append(list(map(str, input())))
for i in seats:
    if (i[0] == free and i[1] == free):
        print("YES")
        i[0] = "+"
        i[1] = "+"
        print_seats(seats)
        break
    elif (i[3] == free and i[4] == free):
        print("YES")
        i[3] = "+"
        i[4] = "+"
        print_seats(seats)
        break
else:
    print("NO")

