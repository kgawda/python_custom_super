"""
Zadanie: napisać skrypt, który odczytuje csv_example2.csv
i dla każdej jego linijki drukuje na konsoli user_label i MO.
Np.:
34_XYZ1234A_101L18_O_ABC EUtranCellFDD=0
34_XYZ1234A_201L18_O_ABC EUtranCellFDD=1
34_XYZ1234A_301L18_O_ABC EUtranCellFDD=2
...
"""

def main():
    with open("csv_example2.csv") as f:
        # n = 0
        # for linia in f:
        #     ...
        #     n += 1

        for n, linia in enumerate(f):
            if n == 0:
                continue
            linia = linia.rstrip()
            elementy = linia.split(";")
            print(elementy[4], elementy[0])


if __name__ == "__main__":
    main()
