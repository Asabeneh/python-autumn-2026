
a = -5 # a store the value 5
if a > 0: # the condition here
 print(f'{a} is a positive integer')
elif a == 0:
 print(f'{a} is zero')
else:
 print(f'{a} is a negative integer')


 is_raining = False 

 if is_raining:
  print('Go with an umbrella')
 else:
  print('Go out freely it seems such a shinny day.')


""" weather = input('What is the weather like? ').lower()

if weather == 'rainy':
 print('Go with a raincoat or an umbrella')
elif weather == 'sunny':
 print('Go out freely')
elif weather == 'cloudy':
 print('There is a possibility of rain')
elif weather.lower() == 'foggy':
 print('Visibility might be hindered')
elif weather == 'snowy':
 print('It could be slippery')
elif weather == 'stormy':
    print('You should be very careful, it could storm today.')
else:
 print('No one knows the weather') """
 
 
 
weather = input('What is the weather like? ').lower()

match weather:
    case 'rainy':
        print('Go with a raincoat or an umbrella')
    case 'sunny':
        print('Go out freely')
    case 'cloudy':
        print('There is a possibility of rain')
    case 'foggy':
         print('Visibility might be hindered')
    case 'snowy':
        print('It could be slippery')
    case 'stormy':
         print('You should be very careful, it could storm today.')
    case _:
         print('No one knows the weather')
        
    
        
