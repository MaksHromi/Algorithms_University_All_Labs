def wynik(i):
    if i < 3:
        return 1
    elif i % 2 == 0:
        return wynik(i-3) + wynik(i-1) + 1
    else:
        return wynik(i-1) % 7