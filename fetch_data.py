import requests
import json

API_KEY = 'JHFa6EPnJSGkGPoHs9bxPky5dXIAAz36'
QUERY_ID = '3930803'
BASE_URL = 'https://api.dune.com/api/v1/query/'

response = requests.get(f'{BASE_URL}{QUERY_ID}/results', headers={'x-dune-api-key': API_KEY})
data = response.json()

with open('data.json', 'w') as f:
    json.dump(data, f)
