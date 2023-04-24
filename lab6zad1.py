a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

for i in range(a, b+1):
    if i % 2 == 0:
        print(i)

for i in range(b, a-1, -1):
    if i % 2 != 0:
        print(i)