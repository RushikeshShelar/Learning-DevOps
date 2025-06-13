import requests

# Simple POST request to a public API
url = 'https://httpbin.org/post'
data= {
    'username': 'rushikesh', 
    'password': '12345'
}
response = requests.post(url, data=data)
print(response.status_code)
print(response.json())