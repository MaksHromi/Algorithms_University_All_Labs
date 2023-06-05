def calculateBinomialCoefficient(m, n):
    memo = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if j == 0 or j == i:
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]

    return memo[m][n]

m = 5
n = 3
result = calculateBinomialCoefficient(m, n)
print(f"Współczynnik dwumianowy C({m}, {n}) wynosi: {result}")