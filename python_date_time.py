'''
Time


'''

from datetime import datetime
# time = datetime(2026, 11, 16, 8, 30, 45)
now = datetime.now()
now = datetime(2026, 11, 16, 14, 30, 45)
print(now)
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
print(f'{day}/{month}/{year}')
print(f'{day}-{month}-{year}')
print(f'{day}.{month}.{year}')

formatted_time = now.strftime('%a %b %#d, %Y %I:%M %p')
print(formatted_time)
print(type(formatted_time))

date_string = "5 December, 2019"
print(type(now))
time_obj = datetime.strptime(date_string, "%d %B, %Y")
print(type(time_obj))

from datetime import date, datetime
today = date(year=2026, month=11, day=17)
new_year = date(year=2027, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)  # Time left for new year:  27 days, 0:00:00


t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00




