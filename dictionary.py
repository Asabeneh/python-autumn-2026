'''
Dictionary is a key value pair type of Python data type


'''
from pprint import pprint
import copy
empty_dct =  {}
print(type(empty_dct))

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'is_married':True,
    'mass':75,
    'height':1.72,
    'skills':['HTML','CSS','JavaScript','Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

print(person['first_name'])
print(person.get('first_name'))
print(person['last_name'])
print(person.get('last_name'))
# print(person['age'])
print(person.get('age'))

if 'age' in person:
    print(person['age'])
else:
    person['age'] = 75
    print('Age has been added')
    # print('Age does not exist')

print(person)

print(person['skills'])
person['skills'].append('Databases')
print(person['skills'])
print(person)
person['country'] = 'Finland'
pprint(person)

for key in person:
    print(key, person[key])

items = person.items()
print(items)
""" for item in items:
    key, value = item
    print(key, value) """
for key, value in items:
    print(key, value)


keys = person.keys()
print(keys)
values = person.values()
print(values)
print(len(person))

person['email'] = 'asab@gmail.com'
pprint(person)
person['age'] = 50

pprint(person)

print('nationality' in person)
print('age' in person)

person.popitem()
pprint(person)
person.pop('age')
pprint(person)

del person['mass']
pprint(person)
# person.clear()
# print(person)
person_copy = copy.deepcopy(person)
person_copy['skills'].append('ML and AI')
pprint(person)
pprint(person_copy)

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy['name'] = 'Asab'
print(dct)
print(dct_copy)