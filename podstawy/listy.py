def main():
    lista = [1, 2, 3]
    lista_str = ["Ala", "ma", "kota"]
    lista_mix = ["Ala", 2, True, None, [1, 2]]
    lista_pusta = []

    assert len(lista) == 3
    assert not lista_pusta
    assert 2 in lista
    assert "ma" in lista_str
    assert ["Ala", "ma"] not in lista_str  # inaczej niż dla str!

    assert lista + lista_str == [1, 2, 3, 'Ala', 'ma', 'kota']
    assert lista * 2 == [1, 2, 3, 1, 2, 3]

    lista.append(4)
    assert lista == [1, 2, 3, 4]
    # Nie da się dodać do listy w ten sposób:
    # lista[4] = 5  # IndexError: list assignment index out of range

    assert lista.pop() == 4
    assert lista == [1, 2, 3]

    assert lista_str == ["Ala", "ma", "kota"]
    lista_str[2] = "borsuka"
    assert lista_str == ["Ala", "ma", "borsuka"]

    # indeksy:
    #    0      1       2
    # ["Ala", "ma", "borsuka"]
    #   -3     -2      -1

    assert lista_str[-1] == "borsuka"



if __name__ == "__main__":
    main()
