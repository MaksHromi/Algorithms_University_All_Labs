def number_sort(numbers, new_number):
    numbers.append(new_number)
    numbers.sort()
    return numbers

numbers = [1, 3, 5, 7, 9]
new_number = 6

sorted_numbers = number_sort(numbers, new_number)
print(sorted_numbers)
print(numbers)