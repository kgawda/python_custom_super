def main():
    slownik = {1: "Kot", 2: "Pies"}
    assert slownik[1] == "Kot"
    slownik[3] = "Borsuk"  # w list tak nie można!
    assert slownik[3] == "Borsuk"
    assert slownik.get(3) == "Borsuk"

    # slownik[15]  # KeyError: 15
    assert slownik.get(15) is None
    assert slownik.get(15, "brak") == "brak"

    slownik[100] = "Człowiek"

    slownik[1] = "Lew"  # nadpisanie
    assert slownik[1] == "Lew"

    x = slownik.pop(100)  # Usuń "Człowiek"
    assert x == "Człowiek"

    assert len(slownik) == 3

    # {1: "Lew", 2: "Pies", 3: "Borsuk"}
    assert 1 in slownik
    assert "Pies" not in slownik

    # for k in slownik:
    # for k in slownik.keys():  # to samo co wyżej
    # for k, v in slownik.items():
    # for v in slownik.values():

    wartosci = [x for x in slownik.values()]
    assert wartosci == ["Lew", "Pies", "Borsuk"]

    # wartościami może być wszystko
    # kluczami mogą być typy hashowalne (w szczegółności nie-mutowalne)

    # Typy nie-mutowalne są hashowalne, więc możnba użyć jako klucze
    klucze_rozne = {
        123: "OK",
        "String": "OK",
        True: "OK",
        None: "OK",
    }
    # nie można użyć jako kluczy:
    # {
    #     [1, 2]: "błąd",
    #     {1: 11}: "błąd"
    # }



if __name__ == "__main__":
    main()
