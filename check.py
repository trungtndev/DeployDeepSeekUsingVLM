import requests

url = "http://localhost:8080/generate/"
payload = {"prompt": "Tell me a joke"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.json())  # Expected: Model-generated text
