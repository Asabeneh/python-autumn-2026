from countries_data import countries_data
from countries import countries
from pprint import pprint
from functools import reduce
'''
Higher order function: functions that take another function as a parameter or return another function

'''
'''
We will learn the three mainfunctional programming:
map
filter
reduce
'''
nums = [1, 2, 3, 4, 5] # [2, 4, 6, 8, 10]

""" new_lst = []

for num in nums:
    new_lst.append(num * 2)

print(new_lst) """

# new_lst = [num * 2 for num in nums]
# print(new_lst)

new_lst = list(map(lambda num: num * 2, nums))
# print(new_lst)

populations = list(map(lambda country: country['population'], countries_data))
print(populations)
world_population = sum(populations)
print('{:,}'.format(world_population))



""" modified_countries = list(map(lambda country: {
    'name':country['name'],
    'capital':country['capital'],
    'population':country['population']
    }, countries_data))
pprint(modified_countries) """


""" modified_countries = [ {
    'name':country['name'],
    'capital':country['capital'],
    'population':country['population']
    } for  country in countries_data]



pprint(modified_countries) """

modified_countries = []

for country in countries_data:
    modified_countries.append({
    'name':country['name'],
    'capital':country['capital'],
    'population':country['population']
    })
# pprint(modified_countries)

nums = [0, 4, 2, -5, 7, -3, 6, 10]

print(list(map(lambda num: num ** 2, nums)))
print(list(filter(lambda num: num > 0, nums)))
print(list(filter(lambda num: num % 2 == 0, nums)))
print(list(filter(lambda country: 'land' in country, countries)))

nums = [1, 2, 3, 4]
total = 0 # accummulator
for num in nums:
    # num is current
    total = total + num

print(total)

print(reduce(lambda acc, cur: acc + cur, nums, 100))