import fabric

def main():
    connection = fabric.Connection(
        "warsztat.mywire.org",
        user="student",
        connect_kwargs={"password": "_______"}
    )
    connection.run("ls -al")



if __name__ == "__main__":
    main()
