def search_minimum(arr):
    minimum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
    return minimum
arr = [3, 5, 2, 7, 1, 8, 4, 9, 6]
print(search_minimum(arr))