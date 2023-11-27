def main():
    tekst = "Ala ma kota"
    dodatkowy_tekst = " i psa"

    tekst = tekst + dodatkowy_tekst  # konkatenacja
    assert tekst == "Ala ma kota i psa"

    # Porównania == i != nie używamy dla None.
    # Dla None robimy:
    # if tekst is not None:
    # if tekst is None:

    tekst += "!"
    assert tekst == "Ala ma kota i psa!"

    assert type(tekst) == str
    assert str() == ""
    assert str(123) == "123"
    assert str(2+2 == 4) == "True"

    assert tekst.lower() == "ala ma kota i psa!"
    assert tekst.upper() == "ALA MA KOTA I PSA!"
    assert tekst == "Ala ma kota i psa!"

    assert " pies i kot  ".strip() == "pies i kot"
    assert tekst.replace("kota", "borsuka") == "Ala ma borsuka i psa!"
    assert tekst.replace(" ", "-") == "Ala-ma-kota-i-psa!"

    # zwracają bool:
    assert not tekst.isalnum()
    assert "KotPies24".isalnum()

    # zwraca listę:
    assert tekst.split() == ['Ala', 'ma', 'kota', 'i', 'psa!']

    assert len(tekst) == 18  # długość
    pusty_str = ""
    # Równoważne:
    assert len(pusty_str) == 0
    assert pusty_str == ""
    assert not bool(pusty_str)
    assert not pusty_str
    # if not pusty_str:
    #    instrukcje_dla_pustego_stringa()

    # if tekst:
    #    instrukcje_dla_niepustego_stringa()

if __name__ == "__main__":
    main()
