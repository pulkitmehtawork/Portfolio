import requests

url = 'http://localhost:5000/api'

r = requests.post(url,json={'exp':3,})
print(r.json())