'''
What is string?
It is a data type which is under a single, double, or tripple quote

'''

letter = 'a'
print(letter)
print(type(letter))
print(len(letter))

word = 'Python'
print(type(word), len(word))

sentence = 'Cat is a pet.'
print(sentence, type(sentence), len(sentence))

txt = 'Thirty days of Python'
print(txt)
print(len(txt))
print(txt.upper())
print(txt.lower())
print(txt.title())
print(txt.swapcase())
print(txt.split())

words = txt.split()
print(type(words))
print(words, len(words))
print(txt.startswith('Thirty'))
print(txt.endswith('Python'))

animal = 'Cat' #
print(animal[0])
print(animal[1])
print(animal[2])
print(animal[-1])
print(animal[-2])
print(animal[-3])
print(animal[0:2])
print(animal[1:3])
print(animal[1:])

print(txt.index('days'))
# print(txt.index('z'))
print(txt.index('t'))
print(txt.rindex('t'))

print(txt.find('t'))
print(txt.rfind('t'))
print(txt.find('z'))

first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
city = 'Helsinki'
country = 'Finland'
role = 'Fullstack Engineer'
height = 1.73
# full_name = first_name + ' '+  last_name
full_name = f'{first_name} {last_name}'
print(full_name)

'''
I am Asabeneh Yetayeh. I am a Fullstack Engineer based in Helsinki, Finland. I am 1.73 meter. I am 250 years old.
'''
print('I am ' + full_name + '. ' + 'I am a ' + role + ' base in ' +  city + ', ' + country + '. ' + 'I am '+ str(height) + ' meter. ' + 'I am ' + str(age) + ' years old.')

print(f'I am {full_name}. I am a {role} based in {city}, {country}. I am {height} meter. I am {age} years old.')

print('I am {}. I am a {} based in {}, {}. I am {} meter. I am {} years old.'.format(full_name, role,city, country, height, age))
print('I am %s. I am a %s based in %s, %s. I am %.2f meter. I am %d years old.' %(full_name, role,city, country, height, age))


a  = 3
b = 4
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} x {b} = {a * b}')

# Escape sequences: \, \n, \t, \\

print('I don\'t like to go to the lesson')
print('People say "An apple a day keep the doctor away"')
print("People say \"An apple a day keep the doctor away\"")
print('I love people.\nI love Python too.')
print('Day 1 \t Day 2 \t Day 3')
print('8 \t 12 \t 20')

print('It was impossible to print \\ out.')
print('Finland'[::])
print('Finland'[::-1])
print('')
print('mom' == 'mom'[::-1])

# we have 'Thirty days of Python' on txt variable
print(txt.count('o'))
# ACGA

dna = '''ACAGGCCCTGCGGCGTACATCACTTTGTATGTGCAACGTGCCCAAGTGGCGCCAGGCAAGACTCAGCTGGTTCCTGTGTTAGCTCGAGGCTAGGCATGACAGCTCTTTGAACATGGGCTGGGGGCCTCGAACGGTCGAGAAGCCCATAGTACCTCGGATACCAAGTTGCGCAGGCTATAGCTTGAAGCTGTACTATTTCAGGGGGGGAGCCCTGATGGTCTCTTCTTCTGATGACTCAACTCGCTAGGGTCGTGAAGTCGATTCCTTCGATGGTTAAAAATCAAAGGCTCAGAGTGCAGACTGGAGCGCCCATCTAACGGTTCGCATCTCGAATGCTCGGTCGCCTTTCACATTCCGCGAAAATTCATACCGCTCATTCACTAGGTTGCGAAGTCTACACTGATATATGAATCCGAGCTAGAGCAGGGCTCTTAAAATTCGGAGTCGTTGATGCTCAATACTCCAATCGGTTTTTTCGTGCACCACCGCGAGTGGCTGACAAGGGTTTGACATTGAGTAGCAAGGCAGTTCCGGGCTGAATGAAGCGCCGGGAAAGGTACGCGCCTGGTATGGCAGGATTAAGAAGCCAATACAAAGGCTACATCCTCACTCGGATGGAGGCAAACGCAGAACAATGGTTACTTTTTCGATACGTGAAACATGTCCCACGGTAGCCCAAAGACTTGAGAGTCTATCACCCCTAGGGCCCTTTCCCGGATATAAACGCCAGGTTGAATCCGCATTTGGAGGTACGATGGATCAGTCTGGGTGGGGCGCGCCCCATTTATACCGTGAGTAGGGTCGACCAAGAACCGCAAGATGCGACGGTGTACAAGTAATTGTCAACAGACCATCGTGTTTTCATAATGGTACCAGGATCTTCAAGCCGTGTCAATCAAGCTCGGATTACGGTGTTTACTCCGTCCTGCGGTTACTCACGGTCTGTAATCCACCTCAAGTCAAGCCATTGCCTCTCTGAGACGCCGCATGAATTAATACG'''
print(len(dna))
print(dna.count('A'))
number_of_a = dna.count('A')
total = len(dna)
print( number_of_a / total * 100)

challenge = 'thirty\tdays\tof\tpython'
print(challenge)
print(challenge.expandtabs())
print(challenge.expandtabs(8))
print(challenge.expandtabs(10))

print('abc'.isalpha())
print('abc123'.isalpha())
print('abc'.isalnum())
print('abc123'.isalnum())
print('abc'.isnumeric())
print('123'.isnumeric())

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
print(web_tech)
print(', '.join(web_tech))

