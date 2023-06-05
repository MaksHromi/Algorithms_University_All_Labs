def calculateP(i, j):
    memo = [[0] * (j + 1) for _ in range(i + 1)]

    for x in range(1, i + 1):
        for y in range(1, j + 1):
            memo[x][y] = memo[x - 1][y] + memo[x][y - 1] + 2

    return memo[i][j]


i = 3
j = 4
result = calculateP(i, j)
print(f"Wartość P({i}, {j}) wynosi: {result}")