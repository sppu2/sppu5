N = 4

b = [[0] * N for i in range(N)]

def issafe(i, j):
    for p in range(N):
        if b[i][p] == 1 or b[p][j] == 1:
            return False

    for n in range(N):
        for m in range(N):
            if (i + j == n + m or i - j == n - m) and b[n][m] == 1:
                return False
    return True

def nq(noq):
    if noq == 0:
        return True

    for i in range(N):
        for j in range(N):
            if b[i][j] != 1 and issafe(i, j):
                b[i][j] = 1
                if nq(noq - 1):
                    return True
                b[i][j] = 0
    return False

def printBoard(b):
    for row in b:
        print(row)

if nq(N):
    printBoard(b)
else:
    print("Can't Place")
