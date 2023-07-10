import requests
import sys

query = sys.argv[1]
key = sys.argv[2]

url = 'https://api.todoist.com/sync/v9/quick/add'
payload = {'text': query}
headers = {'Authorization': f'Bearer {key}'}

res = requests.post(url, data=payload, headers=headers)

print(payload)