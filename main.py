import random
import os

clear = lambda: os.system('cls')
# number of rounds
k = 50

o = ['', '', 0]
u = [0] * k
n = 1
# number of players
p = 2

print("Hello! It's Lucky Dice! Press Enter to continue")
input()
table = [''] * p
for i in range(p):
    table[i] = o[::]
    table[i][1] = u[::]
    print(f'Enter the name of player #{i + 1}:')
    x = input()
    table[i][0] = x + ((25 - len(x)) * ' ')
while True:
    table.sort(key=lambda x: x[2], reverse=True)
    print("\033[33m{}\033[0m".format("SCORE"))

    for i in range(p):
        print(table[i][0], *table[i][1], "\033[30m\033[47m{}\033[0m".format(table[i][2]))

    if n == k + 1:
        print("\033[30m\033[43m{}\033[0m".format(table[0][0]), '- WINNER!!!')
        break

    print("\033[33m{}\033[0m".format(f"Round {n}"))
    print("\033[33m{}\033[0m".format("Click ENTER for roll dice"))

    for i in range(p):
        dice = random.randint(1, 666) % 7
        if dice == 0:
            dice += 1
        table[i][1][n - 1] = dice
        table[i][2] = sum(table[i][1])
    n += 1
    input()
    clear()


