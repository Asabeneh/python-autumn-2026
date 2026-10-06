'''
Data Types in Python:
- Numbers(int, float, complex) - Done
- Booleans(True or False)
- Strings
- List
- Tuples
- Sets
- Dictionary
'''

# Numbers

print(10) # -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
print(type(10))

print(9.81, 3.14, type(9.81), type(3.14))

print(2j  + 3, type(2j  + 4))

# Booleans: True or False
print(True, type(True), False, type(False))
print(4 > 3, type(4 > 3), 3 < 2, type(3 < 2))

# Strings: any thing under a single, double or triple quote 
print('a', type('a'))
print('cat', type('cat'))
print('I love people', type('I love people'))
print(len('a'))
print('cat car',len('cat car'))
print("I love people",'''I love people''')

txt = """
A mnemonic is a tool, such as a pattern of letters, a rhyme, or an acronym, used to help the brain remember information.
Common Types and Examples
• Acronyms: Form a new word using the first letter of a list, like HOMES for the Great Lakes (Huron, Ontario, Michigan, Erie, Superior).
• Acrostics: Create a memorable sentence where each word's first letter stands for a fact, like "Please Excuse My Dear Aunt Sally" for the mathematical order of operations (Parentheses, Exponents, Multiplication, Division, Addition, Subtraction).
• Rhymes: Put facts into a short verse, like "I before E, except after C" for spelling rules.
Origin
The word comes from the Ancient Greek word mnēmonikos, meaning "relating to memory," which is tied to Mnemosyne, the Greek goddess of memory. Though it is spelled with an initial "m," the "m" is silent and the pronunciation begins with an "n" sound (ni-MON-ik).
If you'd like, let me know what specific fact or list you are trying to memorize, and I can help you create a custom mnemonic device for it.
"""

# List  - is a collection of indexed, ordered items and it is muttable 

nums = [1, 2, 3, 4]
print(nums, len(nums))
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
last_index = len(nums) - 1
print(nums[last_index])
nums[0] = 1000
print(nums)
nums[last_index] = 'four'

print(nums)

# Tuples: order, indexed, but immuttable/not modifiable

nums = (1, 2, 3, 4)
print(nums, type(nums), len(nums))
print(nums[0])

# Set - a collection items, duplicate is allowed
A = {1, 2, 3, 3, 4, 5, 6}

print(A, len(A))

sentence = 'I love people love is great the love of python is awesome'
print(sentence)
words = sentence.split()
print(words, set(words))
A.add(100)
print(A)
A.update([20, 30, 50, 90])
print(A)

# Dictionary: Key value pair

user = {
    'username':'Asab',
    'email':'asab@example.com',
    'password':'123123',
    'created_at':'6 October 2026 7:53'
}
print(user, len(user))
print(user['email'])