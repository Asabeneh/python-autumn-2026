import json 
from pprint import pprint
from utils import generate_json




new_lst = []
with open('./cats.json') as f:
    data = json.load(f)
    for cat in data:
        dct = {
            'name':cat['name'],
            'country':cat['origin'],
            'weight':cat['weight_average'],
            'life_span':cat['life_span_average']
            }
        new_lst.append(dct)



generate_json(new_lst, 'xyz.json')