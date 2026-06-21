import requests

def get_device_data():

```
url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(
    url,
    timeout=10
)

response.raise_for_status()

return response.json()
```
