import json
import requests


def request_governance(api_url):
    request_url = f"{api_url}/cosmos/gov/v1beta1/proposals"
    api_response = requests.get(request_url)
    json_response = json.loads(api_response.text)
    return json_response