import requests

url = "http://localhost:5000/"

r = requests.get(url=url)
print(r.text)
