import json

class ParsingError(Exception):
    pass

def pierwiatek(x):
    if isinstance(x, str):
        if not x.isdigit():
            raise ParsingError("Only strings made of digits are supportted")
        x = int(x)
    if x < 0:
        # raise Exception("x should be greater or equal to 0")
        raise ValueError("x should be greater or equal to 0")
    return x ** 0.5

def main():
    print("Przed wyjątkiem")
    lista = [1, 2, 3]
    try:
        index = json.loads('{"index: 3}').get("index")
        print(lista[index/0])
        ...
        ...
    except IndexError:
        print("Był wyjątek IndexError")
    except ZeroDivisionError:
        print("Był wyjątek ZeroDivisionError")
    except json.decoder.JSONDecodeError as e:
        print("Błąd", type(e).__name__, e)
    finally:
        # nadal zatrzymuje działanie programu, ale pozwala np. zamknąć połączenie
        print("Inny błąd")

    print("Po wyjątku")

    try:
        pierwiatek("test")
    except ParsingError as e:
        print("Błąd parsowania:", e)

    try:
        pierwiatek(-1)
    except ParsingError as e:
        print("Błąd parsowania:", e)

if __name__ == "__main__":
    main()
