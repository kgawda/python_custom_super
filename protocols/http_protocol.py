import requests

def main():
    response = requests.get("https://www.wp.pl")
    print("Pobrano", len(response.text))
    print(response.status_code)
    print(response.headers)

    response = requests.get("https://www.onet.pl/asdasdsaa")
    print("Pobrano", len(response.text))
    print(response.status_code)
    # response.raise_for_status()  # requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://www.onet.pl/asdasdsaa
    print(response.headers)

if __name__ == "__main__":
    main()
