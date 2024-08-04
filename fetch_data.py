import requests
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

API_KEY = 'JHFa6EPnJSGkGPoHs9bxPky5dXIAAz36'
QUERY_ID = '3930803'

url = f'https://api.dune.com/api/v1/query/{QUERY_ID}/results'
headers = {
    'x-dune-api-key': API_KEY
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad status codes
except requests.exceptions.RequestException as e:
    logging.error(f"Request failed: {e}")
    exit(1)

logging.info(f"Status code: {response.status_code}")

data = response.json()
results = data.get('result', {}).get('rows', [])

if not results:
    logging.warning("No data found in the query results.")
    output = {}
else:
    output = {}
    for result in results:
        badge_name = result.get('badge_name', 'Unknown Badge')
        minted_percentage = result.get('share', 0)
        output[badge_name] = minted_percentage

logging.info(f"Output data to be written to data.json: {output}")

try:
    with open('data.json', 'w') as f:
        json.dump(output, f, indent=4)
    logging.info("Data successfully written to data.json")
except IOError as e:
    logging.error(f"Failed to write to data.json: {e}")
    exit(1)

try:
    with open('data.json', 'r') as f:
        content = f.read()
    logging.info(f"Content of data.json: {content}")
except IOError as e:
    logging.error(f"Failed to read from data.json: {e}")
    exit(1)
