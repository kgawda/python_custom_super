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
    query_two_dbs('SELECT name FROM master.sys.databases', "SHOW DATABASES;")

if __name__ == "__main__":
    main()
