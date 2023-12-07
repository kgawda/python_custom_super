import re

def main():
    s = "Ala ma kota i psa. Sierotka ma rysia. Hej!"
    print(re.findall(r".*\.", s))  # * - wersja zachłanna
    print(re.findall(r".*?\.", s))  # *? - wersja nie zachłanna
    print(re.findall(r"\w+", s))  # słowa, + - 1 lub więcej wystąpień (zachłanny)
    print(re.findall(r"[AEIOUYaeiouy]+", s))  # samogłoski występujące po sobie
    print(re.findall(r"[a-z]+", s))

    # print(re.findall(r"\w{3}", s))  # 3-literowe zbitki
    print(re.findall(r"\w{3,5}", s))  # zbitki od 3 do 5 znaków, zachłanne!

    # print(re.findall(r".*?", s))  # ['', 'A', '', 'l', '', 'a', '', ' ', '', ...
    # print(re.findall(r".*?;", "Ala; pies;kot;;;ryś;"))  # ['Ala;', ' pies;', 'kot;', ';', ';', 'ryś;']

    # \w -> [a-zA-Z0-9_]
    # \d -> [0-9]
    # \s -> [ \t\n\r\f\v]

    print(re.findall(r" (\w{3,5})[\.!]", s))  # ( ) - grupa

if __name__ == "__main__":
    main()
