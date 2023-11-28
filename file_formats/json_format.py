import json
import decimal

def main():
    dane = {
        'liczby': [1, 2, 3],
        "wartosc_logiczna": True,
        "floaty": [0.1, 0.1, 0.1],
        "none": None,
    }
    # zrzucenie do stringa:
    s = json.dumps(dane, indent=4)
    print(s)

    # zrzucenie do pliku:
    with open("example.json", "w") as f:
        json.dump(dane, f, indent=4)

    # Ładowanie:

    dane2 = json.loads(s)
    print(dane2)

    with open("example.json") as f:
        dane2_z_pliku = json.load(f)

    assert dane2 == dane2_z_pliku

    # Przykład pobierania danych ze słownika
    print(max(dane2["liczby"]))
    print(sum(dane2["floaty"]))  # 0.30000000000000004

    dane3 = json.loads(s, parse_float=decimal.Decimal)
    print(dane3)
    print(sum(dane3["floaty"]))  # 0.3

if __name__ == "__main__":
    main()
