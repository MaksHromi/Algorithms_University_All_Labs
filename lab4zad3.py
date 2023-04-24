def znajdzNajwiekszy(tablica):
    if len(tablica) == 0:
        return None
    if len(tablica) == 1:
        return tablica[0]
    polowa = len(tablica) // 2
    lewaPolowa = znajdzNajwiekszy(tablica[:polowa])
    prawaPolowa = znajdzNajwiekszy(tablica[polowa:])
    if lewaPolowa > prawaPolowa:
        return lewaPolowa
    else:
        return prawaPolowa

wektor = [5, 3, 8, 1, 7, 2]
najwiekszy = znajdzNajwiekszy(wektor)
print(najwiekszy)