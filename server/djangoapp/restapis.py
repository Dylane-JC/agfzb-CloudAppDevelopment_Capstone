import requests
import json
from .models import CarDealer
from .models import DealerReview
from requests.auth import HTTPBasicAuth

# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    json_data = {}
    api_key = "TcEHuCixPoEoR3VA6U3zBu82fozLidhmTo-ZNzjnjFfI"
    response = requests.get('https://eu-gb.functions.appdomain.cloud/api/v1/web/f685b25d-91a6-498c-833b-cab9cc0a36d0/api/review/', params=kwargs, headers={'Content-Type' : 'application/json'})
    #if api_key:
    try:
        response = requests.get(url, params=kwargs, headers={'Content-Type' : 'application/json'}, auth=HTTPBasicAuth('apikey', api_key))
    except:
        # If any error occurs
        print("Network exception occuered")

    #status_code = response.status_code
    #print("With status{} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["docs"]
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], 
                                   city=dealer_doc["city"], 
                                   full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], 
                                   lat=dealer_doc["lat"], 
                                   long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], 
                                   zip=dealer_doc["zip"], 
                                   state=dealer_doc["state"])
            results.append(dealer_obj)

    return results

def get_dealer_reviews_from_cf(url, **kwargs):
    results = []
    id = kwargs.get("id")
    if id:
        json_result = get_request(url, id=id)
    else:
        json_result = get_request(url)

    if json_result:
        reviews = json_result["data"]["docs"]

        for dealer_review in reviews:
            #dealer_review = reviews

            review_obj = DealerReview(
                dealership=dealer_review["dealership"],
                name=dealer_review["name"],
                purchase=dealer_review["purchase"],
                review=dealer_review["review"],
                id=dealer_review["id"],
                purchase_date=dealer_review["purchase_date"],
                car_make=dealer_review["car_make"],
                car_model=dealer_review["car_model"],
                car_year=dealer_review["car_year"]                               
                )
            if "id" in dealer_review:
                review_obj.id = dealer_review["id"]
            if "purchase_date" in dealer_review:
                review_obj.purchase_date = dealer_review["purchase_date"]
            if "car_make" in dealer_review:
                review_obj.car_make = dealer_review["car_make"]
            if "car_model" in dealer_review:
                review_obj.car_model = dealer_review["car_model"]
            if "car_year" in dealer_review:
                review_obj.car_year = dealer_review["car_year"]

                sentiment = analyze_review_sentiments(review_obj.review)
                print(sentiment)
                review_obj.sentiment = sentiment
                results.append(review_obj)

    return results

def analyze_review_sentiments(dealerreview):
    url = "https://eu-gb.functions.appdomain.cloud/api/v1/web/f685b25d-91a6-498c-833b-cab9cc0a36d0/api/review/"
    api_key = "TcEHuCixPoEoR3VA6U3zBu82fozLidhmTo-ZNzjnjFfI"
    params = dict()
    get_request('text')
    get_request('version')
    get_request('features')
    get_request('return_analyzed_text')    
    response = requests.get(url, params=params, headers={'Content-Type' : 'application/json'},auth=HTTPBasicAuth('apikey', api_key))
    return response

def post_request(url, json_payload, **kwards):
    print(kwargs)
    print("GET from {} ".format(url))
    json_data = {}
    api_key = "TcEHuCixPoEoR3VA6U3zBu82fozLidhmTo-ZNzjnjFfI"
    if api_key:
        try:
            response = requests.post(url, params=params, json=json_payload, headers={'Content-Type' : 'application/json'}, auth=HTTPBasicAuth('apikey', api_key))
        except:
            # If any error occurs
            print("Network exception occuered")
    else:
        requests.post(url, params=params)
        status_code = response.status_code
        print("With status{} ".format(status_code))
        json_data = json.loads(response.text)
    return json_data
