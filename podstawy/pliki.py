def main():
    # "Gorsze" podejście:
    f = open("listy.py")
    try:
        zawartosc = f.read()
    finally:
        f.close()
    print(len(zawartosc))

    # "Lepsze" podejście - Context Manager:
    with open("listy.py") as f:
        zawartosc = f.read()  # cała zawartość pliku jako jeden string
    print(len(zawartosc))
    # print(repr(zawartosc[:100])) - wydrukuj "reprezentację programistyczną" pierwszych 100 znaków

    licznik = 0
    with open("listy.py") as f:
        for linia in f:
            # linia = linia.strip()  # zjada białe znaki z początku i końca
            linia = linia.rstrip()  # zjada białe znaki z końca stringa
            licznik += len(linia)
            print("Przeczytałem linię:", linia)

    print("W sumie znaków (bez kończących whitespace):", licznik)

if __name__ == "__main__":
    main()
