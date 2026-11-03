
""" names = []
while True:
    name = input('Enter you name:')
    if name =='q' or name == 'quit':
        break
    names.append(name)
print(names) """

count = 1
while count < 101:
    print(count)
    count = count  + 2
    
count = 10

while count > -1:
    print(count)
    count  = count - 1
    
nums = []
while True:
    value = int(input('Enter number: '))
    if value == 0:
        break 

    if value < 0:
        continue
    nums.append(value)
print(nums) 
    
