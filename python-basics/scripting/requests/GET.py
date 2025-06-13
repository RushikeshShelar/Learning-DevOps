import requests

# Simple GET request to a public API
response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())

# GET request with parameters
url = 'https://api.github.com/search/repositories'
params = {
    'q': 'python',
    'sort': 'stars',
    'order': 'desc',
    'per_page': 1
}
# response = requests.get(url, params=params)
# print(response.status_code)
# print(response.json())
