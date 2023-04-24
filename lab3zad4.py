number = int(input("Enter the number: "))
result = []

while number > 0:
    if number % 2 == 0:
        result.append("0")
    else:
        result.append("1")
    number //= 2

result.reverse()
binary_number = "".join(result)
print(binary_number)