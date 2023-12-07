def main():
    user = "Adam"
    user_id = 123
    target = "Użytkownik Adam, id 123"
    # print("Użytkownik", user+",", "id", user_id)

    s1 = "Użytkownik " + user + ", id " + str(user_id)
    assert s1 == target

    s2 = "Użytkownik %s, id %d" % (user, user_id)  # może być %s zamiast %d
    assert s2 == target

    s3 = "Użytkownik {}, id {}".format(user, user_id)
    assert s3 == target

    s4 = "Użytkownik {user_name}, id {user_id}".format(user_name=user, user_id=user_id)
    assert s4 == target

    data = {"user_name": user, "user_id": user_id}
    s4a = "Użytkownik {user_name}, id {user_id}".format(**data)  # ** - odpakowanie słownika
    assert s4a == target

    s5 = f"Użytkownik {user}, id {user_id}"
    assert s5 == target

    print(f"Wynik = {2 + 2}")
    print(f"Nåme = {user.replace('a', 'å')}")
    print(f"Wynik = {1/3:.2f}")  # zaokrąglenie do 2 miejsc po przeciunku
    print(f"Wynik = {user!r}")  # zwraca repr z wartości


if __name__ == "__main__":
    main()
