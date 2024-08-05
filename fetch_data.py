from dune_client.client import DuneClient
import json

API_KEY = 'JHFa6EPnJSGkGPoHs9bxPky5dXIAAz36'
QUERY_ID = 3930803

dune = DuneClient(API_KEY)
query_result = dune.get_latest_result(QUERY_ID)

if query_result:
    results = query_result['result']['rows']
    output = {result['badge_name']: result['share'] for result in results}
    
    print("Output data to be written to data.json:", output)

    with open('data.json', 'w') as f:
        json.dump(output, f)

    with open('data.json', 'r') as f:
        content = f.read()
        print("Content of data.json:", content)
else:
    print("No results found")
