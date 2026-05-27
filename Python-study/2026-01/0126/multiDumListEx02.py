table = []


def printlist(twoDL):
    for row in range(len(twoDL)):
        for col in range(len(twoDL[0])):
            print(twoDL[row][col], end=" ")
        print()


def init(twoDL):
    for row in range(len(twoDL)):
        for col in range(len(twoDL[0])):
            if (row + col) % 2 == 0:
                twoDL[row][col] = 1


for row in range(10):
    table.append([0] * 10)

init(table)
printlist(table)
