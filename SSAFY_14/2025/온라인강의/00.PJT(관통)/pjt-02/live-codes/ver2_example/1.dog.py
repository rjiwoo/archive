import requests

url = 'https://dog.ceo/api/breeds/image/random'

response = requests.get(url).json()
print(response)
