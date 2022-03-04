"""Sereja and Dima"""
n = int(input())
cards = list(map(int, input().split()))
player1 = 0
player2 = 0
turn = 0
for i in range(n):
    if not cards:
        break
    if turn == 0:  # Player1 turn.
        if cards[0] > cards[-1]:
            player1 += cards[0]
            cards.remove(cards[0])
        else:
            player1 += cards[-1]
            cards.remove(cards[-1])

    elif turn == 1:  # Player2 turn
        if cards[0] > cards[-1]:
            player2 += cards[0]
            cards.remove(cards[0])
        else:
            player2 += cards[-1]
            cards.remove(cards[-1])
    turn ^= 1
print(f"{player1} {player2}")
