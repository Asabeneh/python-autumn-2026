from countries import countries

def add_two_numbers(a, b):
    return a  + b

def make_square(n):
    return n * n

def add_ten(n):
    return n  + 10
    
def filter_countries_with_land(data):
    lst = []
    for country in data:
        if 'land' in country:
            lst.append(country)
    return lst

def filter_evens(nums):
    evens = []  
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens

def calcualte_weight(mass, gravity = 9.81):
    return round(mass * gravity)

def sum_numbers(*args):
    print(args)
    return sum(args)

def get_person_info(first_name, last_name, age, country, city, role):
    return f'He is {first_name} {last_name}. He is {age}, and from {city},{country}. He is a {role}.'

