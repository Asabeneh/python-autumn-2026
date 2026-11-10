from countries import countries
from countries_data import countries_data
nums = [1, 2, 3, 4, 5] # [2, 4, 6, 8, 10]

""" new_lst = []
for num in nums:
    new_lst.append(num  * 2)

print(new_lst) """

new_lst = [num * 2 for num in nums]
print(new_lst)

countries_with_land = [country.upper() for country in countries if 'land' in country]
print(countries_with_land)

lst_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # to change this a flat list

""" flat_lst = []
for lst in lst_lst:
    for item in lst:
        flat_lst.append(item)
print(flat_lst) """

""" flat_lst = []
for lst in lst_lst:
    flat_lst.extend(lst)
print(flat_lst) """

flat_lst = [item for lst in lst_lst for item in lst]
print(flat_lst)


languages = []
for country in countries_data:
    languages.extend(country['languages'])

print(languages, len(languages), len(set(languages)))
  