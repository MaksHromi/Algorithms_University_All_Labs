def merge(list1, list2):
    list = []
    i = 0
    j = 0

    while i < len(list1) or j < len(list2):
        if i < len(list1) and (j >= len(list2) or list1[i] < list2[j]):
            list.append(list1[i])
            i += 1
        else:
            list.append(list2[j])
            j += 1

    return list

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

list = merge(list1, list2)
print(list)