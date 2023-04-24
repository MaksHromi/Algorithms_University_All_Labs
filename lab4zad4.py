def policzSume(tablica):

    if len(tablica) == 0:
        return 0
    if len(tablica) == 1:
        return tablica[0]

    polowa = len(tablica) // 2
    lewaPolowa = policzSume(tablica[:polowa])
    prawaPolowa = policzSume(tablica[polowa:])
    return lewaPolowa + prawaPolowa

tablica = [5, 3, 8, 1, 7, 2]
suma = policzSume(tablica)
print(suma)