
'''
for

'''
from cats_data import cats

for country in ['Finland','Sweden', 'Norway']:
    print(country)
    

for i in range(3):
    print('Hello world! Life is good!')
    
    


""" print('Name\t\tOrign\t\tLife Span\tWeight')
for cat in cats:
    print(f'{cat['name']}\t\t{cat['origin']}\t\t{cat['life_span_average']}\t{cat['weight_average']}') """
    

years_total = 0 
number_cats = len(cats) 
for cat in cats:
    life_span = cat["life_span_average"]
    years_total = years_total + life_span

average = years_total / number_cats
print(average)
