import requests
import json

# вызов api and save
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"status code{r.status_code}")

# Analys sctructure data
response_dict = r.json()
readable_file = 'read_hh_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
