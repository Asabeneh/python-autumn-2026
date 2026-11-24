

from pprint import pprint
from utils import fetch_data, generate_json

url = 'https://hello-flask-hazel.vercel.app/v1/api/cats'

cats = fetch_data(url)


new_lst = []
for cat in cats:
    dct = {
        'name':cat['name'],
        'country':cat['origin'],
        'weight':cat['weight_average'],
        'life_span':cat['life_span_average']
        }
    new_lst.append(dct)
generate_json(new_lst, 'cats-fetched-simplifed.json')