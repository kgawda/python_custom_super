import logging

def pierwiastek(x):
    logging.debug("Liczę pierwiastek z %s", x)
    return x ** 0.5

def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s: %(message)s',
        ## Pisanie do pliku:
        # filename="app.log",
        # encoding='utf-8'
    )
    # Wywołać najwcześniej jak się da. Można wywołać tylko raz.

    logging.debug("Wydruk debugowy")
    logging.info("Mówię co robię")
    logging.warning("Uwaga! Ostrzeżenie")
    logging.error("Błąd! ...")

    try:
        1/0
    except ZeroDivisionError:
        # logging.error("Dzielenie przez zero", exc_info=True)
        # ... lub to samo, ale krócej:
        logging.exception("Dzielenie przez zero")

    pierwiastek(1)


if __name__ == "__main__":
    main()
