def calculateS(n):
    memo = [0] * (n + 1)

    memo[0] = 1
    memo[1] = 1

    for i in range(2, n + 1):
        memo[i] = 2 * memo[i - 1] - memo[i - 2]

    return memo[n]

n = 5
result = calculateS(n)
print(f"N-ty wyraz ciągu S({n}) wynosi: {result}")
