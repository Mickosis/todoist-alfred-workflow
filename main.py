import requests
import sys
import os

query = sys.argv[1]
key = sys.argv[2]

url = 'https://api.todoist.com/sync/v9/quick/add'
payload = {'text': query}
headers = {'Authorization': f'Bearer {key}'}

res = requests.post(url, data=payload, headers=headers)

print(res.status_code)
print(payload)
print(headers)
if res.status_code == 200:
	os.system('afplay /System/Library/Sounds/Purr.aiff')