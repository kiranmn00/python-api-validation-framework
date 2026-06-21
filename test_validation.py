from api_client import get_device_data
from validator import validate_response

data = get_device_data()

results = validate_response(data)

for check, status in results:
    print(f"{check}: {status}")
