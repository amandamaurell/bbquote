import requests

def get_quote():

    url = "https://movie-quote-api.herokuapp.com/v1/quote/"
    response = requests.get(url).json()
    return f"'{response['quote']}' \n> {response['role']}"


if __name__ == "__main__":
    print(get_quote())