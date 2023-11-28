import fabric

def main():
    connection = fabric.Connection(
        "warsztat.mywire.org",
        user="student",
        connect_kwargs={"password": "____"}
    )

    # Wywołanie i analiza komendy
    result = connection.run("free", hide=True)
    command_output = result.stdout
    available_mem = int(command_output.splitlines()[1].split()[-1])
    print("Available memory", round(available_mem/1024), "MiB")

    # Pobieranie pliku przez scp:
    connection.get(
        "/home/student/data.txt",
        # local="downloaded.txt"
    )

    connection.close()



if __name__ == "__main__":
    main()
