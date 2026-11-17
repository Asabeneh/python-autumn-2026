import requests
from pprint import pprint
url = 'https://hello-flask-hazel.vercel.app/v1/api/cats'

response = requests.get(url)
cats = response.json()
# pprint(cats)

for cat in cats:
    print(cat['origin'], cat['life_span_average'])