import re

def main():
    with open("txt_example1.txt") as f:
        s = f.read()

    # Zad., cz1. Zanlazeźć wszystkie Cell Name w pliku
    #   Np.: 34_XYZ1234A_101L18_O_ABC
    # Zad., cz2. Wyciągnąć za pomocą groups poszczególne elementy z Cell Name

    # for cell in re.findall(r"(\d{2})_([A-Z0-9]{8})_(\d{3})([A-Z]\d{2})\w*", s):
    #    print(cell)

    for region, cell_id, sector, tech in re.findall(r"(\d{2})_([A-Z0-9]{8})_(\d{3})([A-Z]\d{2})\w*", s):
        print(f"Region {region}: {cell_id}/{sector} radio {tech}")

if __name__ == "__main__":
    main()
