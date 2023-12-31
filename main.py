import requests

API_KEY = open('API_KEY').read()
SEARCH_ENGINE_ID = open('SEARCH_ENGINE_ID').read()

search_query = input('Search...\n')

url = 'https://www.googleapis.com/customsearch/v1'
params = {
    'q' : search_query,
    'key' : API_KEY,
    'cx' : SEARCH_ENGINE_ID
}

response = requests.get(url, params=params)
results = response.json()['items']

#if 'items' in results:
   # print(results['items'][0]['link'])

for item in results:
    print(item['link'])