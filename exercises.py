def calcualte_weight(mass, gravity = 9.81):
    return round(mass * gravity)

mass = 75.5
gravity = 9.81
print(calcualte_weight(mass))
print(calcualte_weight(mass, 1.62))

'''

Write a function called make_square, it takes n parameter and it returns the square of n

'''

def make_square(n):
    return n * n

print(make_square(3))
print(make_square(5))
print(make_square(10))

def add_ten(n):
    return n  + 10

print(add_ten(90))
print(add_ten(10))
'''
How do you sum numbers from 0 to 100

'''
def sum_all_numbers(n):
    total = 0
    for i in range(0, n + 1): # 50 to 100
        total = total + i
    return total

print(sum_all_numbers(100))
print(sum_all_numbers(50))

print()
print('Finland', 'Helsinki','Vantaa','Espoo')

# asterisk packs the argument values to a tuple
def sum_numbers(*args):
    print(args)
    return sum(args)

print(sum_numbers(10, 20, 30, 40, 50, 60, 90, 200))

def get_person_info(first_name, last_name, age, country, city, role):
    return f'He is {first_name} {last_name}. He is {age}, and from {city},{country}. He is a {role}.'

# print(get_person_info(first_name='Asab', country='Finland',last_name='Yeta', city='Helsinki', role = 'Fullstack Engineer', age = 50))
print(get_person_info('Asabeneh','Yetayeh', 50, 'Finland','Helsinki', 'Fullstack Engineer'))


def generate_groups (team, *args):
    print(team)
    print(args)
    for i in args:
        print(i) 
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')

# Pause
def add_three_numbers(a, b, c):
    return a + b + c

print(add_three_numbers(1, 2, 3))
print(add_three_numbers(*[1, 2, 3]))



def arbitrary_named_args(**kwargs):
    print(kwargs)
    print("I received an arbitrary number of arguments, totaling", len(kwargs))
    print("They are provided as a dictionary in my function:", type(kwargs))
    print("Let's print them:")
    for k, v in kwargs.items():
        print(" * key:", k, "value:", v)

arbitrary_named_args(country='Finland', city='Helsinki', population = 5.6)