import requests

def get_device_data():

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    return response.json()
