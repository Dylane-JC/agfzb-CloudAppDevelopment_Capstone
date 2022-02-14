import requests
import json
from .models import CarDealer
from requests.auth import HTTPBasicAuth


# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        response = requests.get(url, headers={'Content-Type' : 'application/json'}, params=kwargs)
    except:
        # If any error occurs
        print("Network exception occuered")
    status_code = response.status_code
    print("With status{} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data
