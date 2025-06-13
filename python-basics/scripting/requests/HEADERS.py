import requests 

headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json",
}
# Example of a GET request with headers with error handling
try:
    response = requests.get('https://api.example.com/data', headers=headers)
    response.raise_for_status() # Raises an HTTPError for bad responses
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

