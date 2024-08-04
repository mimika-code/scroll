import requests
import json

API_KEY = 'JHFa6EPnJSGkGPoHs9bxPky5dXIAAz36'
QUERY_ID = '3930803'

url = f'https://api.dune.com/api/v1/query/{QUERY_ID}/results'
headers = {
    'x-dune-api-key': API_KEY
}

response = requests.get(url, headers=headers)
data = response.json()

results = data.get('data', {}).get('result', [])
output = {}
for result in results:
    badge_name = result['badge_name']
    minted_percentage = result['minted_percentage']
    output[badge_name] = minted_percentage

with open('data.json', 'w') as f:
    json.dump(output, f)
