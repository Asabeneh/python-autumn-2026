'''
print() done
type() done
min() done
max() done
sum() done
str() done
float() done
int() done
input() done
round() done
range()
list()
abs()
'''

# print function takes one or more arguments and it displays it

# Boolean values: False, True

print(10, 'Finland', ['John','David','Robert'], True)

# type is a builtin function that gives you the data type of a certain data
print(type(10), type(9.81), type(2j + 4), type(True), type('Finland'))
print(type([1, 2, 3]), type((1, 2,3)), type({'country':'Finland','city':'Helsinki'}))

print(min(1, 2, 3, -5, 0, 20))
print(max(1, 2, 3, -5, 0, 20))
print(sum([1, 2, 3, -5, 0, 20]))

print('I am ' + str(250) + ' years old.')
print('I am ' + '250' + ' years old.')
print(9, float(9))
print(9.81, int(9.81))
print('lol'*10, int('9') * 10)

# name = input('Enter your name: ')
# number = input('Enter an integer: ')
# print(type(number), float(number), float(number) * 100)

# x = 10
# x += 5 # x = x  + 5
# x *= 10 # x = x * 10
# x /= 15 # x = x / 15
# print(x)


pi = 3.14
radius = 10.15
area = pi * radius * radius
print(area, round(area), round(area, 2))

print(abs(-10))

print(range(0, 11, 1), list(range(0, 101, 1)))

whole_numbers = list(range(0, 101, 1))
evens = list(range(0, 101, 2))
odds = list(range(1, 101, 2))
print(evens)
print(odds)