n = int(input("Podaj liczbę elementów ciągu: "))

suma_dodatnie = 0
suma_ujemne = 0

for i in range(n):
    x = int(input("Podaj kolejny wyraz ciągu: "))
    if x > 0:
        suma_dodatnie += x
    elif x < 0:
        suma_ujemne += x

print("Suma wyrazów dodatnich: ", suma_dodatnie)
print("Suma wyrazów ujemnych: ", suma_ujemne)