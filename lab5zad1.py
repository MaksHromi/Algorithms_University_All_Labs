def fibonacci(n):
    fib_array = [0, 1]

    for i in range(2, n + 1):
        fib_array.append(fib_array[i - 1] + fib_array[i - 2])

    return fib_array[n]

n = 10
result = fibonacci(n)
print(f"Element o indeksie {n} w ciągu Fibonacciego to: {result}")