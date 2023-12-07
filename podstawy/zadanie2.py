import re

def main():
    with open("txt_example1.txt") as f:
        s = f.read()

    # Zad., cz1. Zanlazeźć wszystkie Cell Name w pliku
    # Zad., cz2. Wyciągnąć za pomocą groups poszczególne elementy z Cell Name
    for cell in re.findall(r"...", s):
        print(cell)

if __name__ == "__main__":
    main()
