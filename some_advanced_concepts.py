'''
pack, unpack

We use two operators:

* for tuples
** for dictionaries

'''

def sum_all_nums(*args):
    return sum(args)


print(sum_all_nums(1, 2, 10, 40, -5))

nums = [1, 2, 3, 4, 5]
print(max(1, 2, 3, 4,5))
print(max(*nums))
print(sum(nums))

nums1 = [1, 2, 3]
nums2 = [3, 4, 5]
nums = [*nums1, 0, *nums2]
print(nums)

def get_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'

dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(get_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.
print(get_person_info(name = 'Asabeneh', country = 'Finland', city = 'Helsinki', age = 250))
print(get_person_info('Asabeneh', 'Finland', 'Helsinki', 250))

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
cities = ['Helsinki','Stockholm','Oslo','Copenhagen','Reykjavík']

# for country in countries:
#     print(country)

for i in range(len(countries)):
        rank = i  + 1
        print(f'{rank} - {countries[i]}')

print('This one with enumerate:')
for index, country in enumerate(countries):
    #  index, country = item
     print(f'{index + 1} - {country}')
     
# Zip

print(list(zip(countries, cities)))

for country, city in zip(countries, cities):
     print(country, city)
