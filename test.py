import requests
from requests.api import get

BASE = "http://127.0.0.1:5000/"


response = requests.post(BASE + "note/0", {"title":"Comida", "description":"Lasanha", "date":"Mar 30, 2021"})
response = requests.get(BASE + "note/0")
print(response.json())