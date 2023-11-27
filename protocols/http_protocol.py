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

    # # POST
    # response = requests.post("http://...", data='tutaj dane tekstowe')
    # print(response.status_code)
    # print(response.text)

def challenge():
    # response = requests.get("http://warsztat.mywire.org/Konrad/1/data")
    # print(response.text)

    response = requests.get("http://warsztat.mywire.org/Konrad/2/data")
    data = response.text
    print(data)
    response = requests.post("http://warsztat.mywire.org/Konrad/2/solution", data=data)
    print(response.text)

if __name__ == "__main__":
    main()
    # challenge()  # uncomment to run challenge!
