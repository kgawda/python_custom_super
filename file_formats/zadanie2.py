"""
Zadanie, poziom 1:
Wydrukować po jednym wierszu dla każdej stacji z json_example.json.
Wiersz powinien zawierać: id, short_name, insert_date

Poziom 2:
Powyższe wydrukować w kolejności, posortowane po rosnącym id.
Podpowiedź:
    najpierw napisz funkcję get_id, wyciągającą id dla danego wiersza.
    Potem użyj pętli: for ... in sorted(..., key=get_id)

Poziom 3:
Zamiast insert_date wydrukować czas względny, np. "123 dni temu"
Podpowiedź:
    na początku pliku dodaj: import datetime
    Następnie użyj datetime.datetime.strptime(...)
"""