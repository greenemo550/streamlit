import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")
