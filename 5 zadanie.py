def search_minimum(arr):
    for row in arr:
        minimum = row[0]
        for element in row:
            if element < minimum:
                minimum = element
        row.remove(minimum)
        row.insert(0, minimum)

arr = [[3, 7, 2], [5, 1, 4], [4, 9, 6]]
search_minimum(arr)
print(arr)