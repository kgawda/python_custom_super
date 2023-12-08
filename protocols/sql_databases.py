import os
import pymysql
import pymysql.cursors
import pymssql

USER_NUMBER = int(os.environ.get("USER_NUMBER"))
PASSWORD = os.environ.get("PASSWORD")
"""
On Windows Command Prompt:
    set "USER_NUMBER=11" 
    set "PASSWORD=..."
"""

def test_mysql(query):
    with pymysql.connect(
        host="warsztat.mywire.org",
        user="root",
        port=5300 + USER_NUMBER,
        password=PASSWORD,
        db="skoki",
        cursorclass=pymysql.cursors.DictCursor,
        charset='utf8mb4',
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)
        connection.commit()

def test_mssql(query):
    with pymssql.connect(
        server="warsztat.mywire.org",
        user="sa",
        port=5400 + USER_NUMBER,
        password=PASSWORD,
        database="skoki",
    ) as connection:
        with connection.cursor(as_dict=True) as cursor:
            cursor.execute(query)
            for row in cursor:  # bez fetchall!
                print(row)
        connection.commit()

def query_two_dbs(mssql_query, mysql_query):
    if mssql_query:
        print("=== MS SQL ===")
        test_mssql(mssql_query)
    if mysql_query:
        print("=== MySQL ===")
        test_mysql(mysql_query)

def main():
    # query_two_dbs('SELECT name FROM master.sys.databases', "SHOW DATABASES;")
    # query_two_dbs('', "SELECT 4+4")  # --> 8  # na MS SQL nie zadziała z AsDict
    # query_two_dbs('', "SELECT 3, 4, 5")
    # query_two_dbs('SELECT * FROM zawodnicy', "SELECT * FROM zawodnicy")
    # query_two_dbs('SELECT imie, nazwisko FROM zawodnicy', "SELECT imie, nazwisko FROM zawodnicy")
    # query_two_dbs(
    #     'SELECT nazwisko, waga / POWER(wzrost/100.0, 2) AS bmi FROM zawodnicy',  # Uwaga! w MS SQL int/int -> int
    #     "SELECT nazwisko, waga / POW(wzrost/100, 2) AS bmi FROM zawodnicy"
    # )
    # query_two_dbs("SELECT imie + ' ' + nazwisko AS nazwa FROM zawodnicy", "SELECT concat(imie, ' ', nazwisko) FROM zawodnicy")
    # query_two_dbs('SELECT nazwisko FROM zawodnicy WHERE wzrost>180', "SELECT nazwisko FROM zawodnicy WHERE wzrost>180")
    # query_two_dbs("SELECT nazwisko_t FROM trenerzy WHERE data_ur_t IS NULL AND kraj <> 'JPN'", "SELECT nazwisko_t FROM trenerzy WHERE data_ur_t IS NULL AND kraj <> 'JPN'")
    # query_two_dbs("SELECT kraj, imie, nazwisko FROM zawodnicy ORDER BY kraj DESC, nazwisko", "SELECT kraj, imie, nazwisko FROM zawodnicy ORDER BY kraj DESC, nazwisko")
    # query_two_dbs("SELECT kraj, COUNT(*) AS ilosc FROM zawodnicy GROUP BY kraj", "SELECT kraj, COUNT(*) FROM zawodnicy GROUP BY kraj")
    # query_two_dbs(
    #     "SELECT kraj, AVG(wzrost) AS sr_wzrost FROM zawodnicy GROUP BY kraj HAVING AVG(wzrost)>=180", # Uwaga! MS SQL AVG() -> int
    #     "SELECT kraj, AVG(wzrost) FROM zawodnicy GROUP BY kraj HAVING AVG(wzrost)>=180"
    # )
    query_two_dbs("SELECT * FROM zawody", "SELECT * FROM zawody")
    query_two_dbs(
        "SELECT data, miasto FROM zawody JOIN skocznie ON zawody.id_skoczni = skocznie.id_skoczni",
        "SELECT data, miasto FROM zawody JOIN skocznie ON zawody.id_skoczni = skocznie.id_skoczni"
    )
    # query_two_dbs("INSERT INTO zawody VALUES (4, 8, '2023-12-24')", "INSERT INTO zawody VALUES (4, 8, '2023-12-24')")

"""
Uwaga! Powyższe zapytania są stringami dla czytelności.
W rzeczywistości, jeśli dostarczamy do bazy wartości pobrane ze świata zewnętrznego (np. formularz www),
należy je podać osobno, żeby uniknąć SQL Injection. Np.:

        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
"""

if __name__ == "__main__":
    main()
