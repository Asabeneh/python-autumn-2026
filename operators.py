# Arithmetic operators:+, -, *,/, //, **, %

print(3 + 4)
print(4 - 3)
print(4 * 3)
print(4 / 3)
print(2 ** 3)
print(4 ** 0.5)
print(5 % 4)
print(9 % 3)
print(9 // 4)
print(9 // 3)
print(7 // 6)
print(3 // 4)

'''
Operators:
- Assignment: =
- Arithmetic: +, -, *, /, %, //, **
- Comparison: >, >=, <, <=, !=
- Logical Operators: or, and, not
'''
# Assignment operators: =,+=, -=, *=

a = 4
print(a)
a *=  10
print(a)

# Comparison operators: >, >=, <, <=, !=

print(4 > 3)
print(4 >= 3)
print(4 < 3)
print(4 <= 3)
print(3 <= 3)
print(3 == '3')
print(str(3) == '3')
print(3 == int('3'))
print(3 != '3')

# Logical Operators: or, and, not
print(' ==== LOGICAL OPERATORS or =====')
print(4 > 3 or 2 > 0)
print(4 > 3 or 2 < 0)
print(4 < 3 or 2 < 0)

print('====== and ======')
print(4 > 3 and 2 > 0)
print(4 > 3 and 2 < 0)
print(4 < 3 and 2 < 0)

print('====== not ======')
print(True, False)
print(not True == False)
print(not 4 > 3 and 2 > 0)
print(not not True)

print('Fin' in 'Finland')
print('land' in 'Finland')
print('Finland' in ['Finland','Sweden','Norway','Denmark','Iceland'])

print(2 is 2)
print(2 is not 3)