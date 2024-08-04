import requests
import json

API_KEY = 'JHFa6EPnJSGkGPoHs9bxPky5dXIAAz36'
QUERY_ID = '3930803'

url = f'https://api.dune.com/api/v1/query/{QUERY_ID}/results'
headers = {
    'x-dune-api-key': API_KEY
}

response = requests.get(url, headers=headers)

print("Status code:", response.status_code)
if response.status_code != 200:
    print("Error:", response.text)
else:
    data = response.json()
    print("Received data:", data)

    results = data.get('result', {}).get('rows', [])
    output = {}
    for result in results:
        badge_name = result['badge_name']
        minted_percentage = result['share']
        output[badge_name] = minted_percentage

    print("Output data to be written to data.json:", output)

    with open('data.json', 'w') as f:
        json.dump(output, f)

  
    with open('data.json', 'r') as f:
        content = f.read()
        print("Content of data.json:", content)
