from countries import countries

nums = [1, 2, 3, 4]

for num in nums:
    print(num)
    
# countries = ['Finland','Sweden','Norway','Denmark','Iceland']

countries_with_land = []
for country in countries:
    if 'land' not in country:
        countries_with_land.append(country)
print(countries_with_land)
    

for country in countries:
    if country.startswith('S'):
        print(country)
        

countries_with_stan = []
for country in countries:
    if country.endswith('stan'):
        countries_with_stan.append(country)
print(countries_with_stan)

nums = [0, 3, 2, 4, -5, 6, 9, 10]
total = 0
for num in nums:
    total = total + num
    
print(total)
  
positive_numbers = []   
for num in nums:
    if num > 0:
        positive_numbers.append(num)
print(positive_numbers)   
  

negative_numbers = []   
for num in nums:
    if num < 0:
        negative_numbers.append(num)
print(negative_numbers)      

evens = []  
odds = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)
print(evens) 
print(odds)

# break, continue

print('Let us how break works')
for num in nums:
    if num < 0:
        break
    print(num)
    
print('Let us how continue work')
for num in nums:
    if num < 0:
        continue
    print(num)
        
        
for i in range(4):
    print(i)

       
print(list(range(0, 101, 5))) 

for i in range(0, 10, 1):
    print(i)
    
    
    
print(list(range(10, -1, -1)))

for i in range(10, -1, -1):
    print(i)

    