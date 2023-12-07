from datetime import datetime, timezone
from lxml import etree

def main():
    root = etree.fromstring("<a><b><c>Hej!</c><c/></b></a>")
    root2 = etree.parse("xml_example.xml").getroot()
    assert type(root) == type(root2)

    # <Objects total='3' offset='0'>
    print(root2.get("total"))  # -> str '3'
    # for x in root2:  # przejdzie po wszystkich tagach potomnych
    for x in root2.iter("Object"):  # przejdzie po tagach potomnych o nazwie Object
        ack_time = x.get("ackTime")
        ack_datetime = datetime.strptime(ack_time, "%Y-%m-%d %H:%M:%S.%f")
        if ack_datetime.year == 1970:
            ack_datetime = None
        changed_at = x.get("changedAt")
        changed_datetime = datetime.fromtimestamp(int(changed_at)/1000)
        print(x.tag, ack_datetime, changed_datetime)

    for x in root: # tylko "b"
    # for x in root.iter():  # a, b i c
    # for x in root.iter("c"):  # wszystkie c
    # for x in root.iterfind("c"): # sprawdzi tylko bezpośrednich potomków - nic nie zwróci!
        print(x)

    c = root.find("b").find("c")
    print(c.text)  # "Hej!"
    c.text = "Inny tekst"
    c.set("atrybut", "wartosc")

    print(etree.tostring(root, pretty_print=True, encoding='utf-8'))


def dygresja_strefy_czasowe():
    now = datetime.now(timezone.utc)  # zamiast datetime.utcnow()
    date1 = datetime.strptime('2023-05-17 15:14:30.660', "%Y-%m-%d %H:%M:%S.%f")  # Musimy wiedzieć, z jakiej strefy czasowej jest ten czas
    date1 = date1.replace(tzinfo=timezone.utc)

    print(now.astimezone(), date1.astimezone())


if __name__ == "__main__":
    main()
    # dygresja_strefy_czasowe()
