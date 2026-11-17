try:
    print('I am the try block')
    print('1' + 3)
except TypeError:
    print('A type error')
except Exception as e:
    print(e)
else:
    print('I will be printed out with try block')
finally:
    print('I will be printed out all the time')


try:
    a = int(input('Enter an integer: '))
    if a > 0:
        print(f'{a} is a positive number')
    elif a == 0:
        print(f'{a} is a zero')
    elif a < 0:
        print(f'{a} is a negative number')
except:
    print('Value should be a number')


try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    current_year = 2026
    age = current_year - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print('Year born should be a number')
