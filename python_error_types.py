
'''
It will raise a syntax error
print("Hello') 
'''
print('Hello') 
print("Hello")

'''
How about if we unnecesary indentation
 print("Hello")

 It raises IndentationError 
'''

print("Hello")

'''
What is the problem if try to add a number and a string
print(1 + '2')

It raises a type error
'''
print(1 + 2)
print(1 + int('2'))

print('1' + '2')
print(str(1) + '2')

'''
What will be the result for this? Does it raise an error?
nums = [1, 2, 3]
print(nums[3])
It will raise an index error
'''
nums = [1, 2, 3]
print(nums[2])

'''
user = {
'name':'Asab',
'age':50,
}
user['gender']

'''
user = {
'name':'Asab',
'age':50,
}
# print(user['gender'])
print(user.get('gender'))

'''
How about if try to access a variable that doesn't exist
print(age)

It will rain a name error
'''
age = 50
print(age)

'''
How about if we import a module that does exist?

import maths
print(math.sqrt(2))
It raises module not found:ModuleNotFoundError
'''
import math
print(math.sqrt(2))


# print(math.PI) # cause a attribute error
print(math.pi)

'''
How about if we try to import something that does exist
It raises an ImportError
'''

from math import pow

print(pow(2, 3))

print(int('2'))
# print(int('a')) # it raises value error

'''
print(1 / 0)
It raises ZeroDivisionError
'''