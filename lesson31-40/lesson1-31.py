import requests

def fetch_users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    if response.status_code == 200:
        users = response.json()
        for user in users:
            print(f"Name: {user['name']}, Email: {user['email']}")
    else:
        print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")

fetch_users()
