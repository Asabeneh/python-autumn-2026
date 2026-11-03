from countries import countries

'''
Builtin Functions: print(), len(), round(), input()
Custom Functions:

'''

def do_something (task):
    print(f'I am {task}.')
    
    
do_something('teaching')
do_something('learning')
do_something('singing')
do_something('running')


def add_two_numbers(a, b):
    return a  + b
    
print(add_two_numbers(3, 4))
print(add_two_numbers(30, 40))
print(add_two_numbers(-3, 4))

def filter_countries_with_land(data):
    lst = []
    for country in data:
        if 'land' in country:
            lst.append(country)
    return lst

print(filter_countries_with_land(countries))


def filter_evens(nums):
    evens = []  
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens

nums = [0, 3, 2, 4, -5, 6, 9, 10]
print(filter_evens(nums))