def check_value(arr, value):
    if value in arr:
        return True
    else:
        return False

array = [1, 2, 3, 4, 5]
value = int(input("Podaj wartość:"))
if check_value(array, value):
    print("Wartość jest zawarta w tablicy")
else:
    print("Wartość nie jest zawarta w tablicy")