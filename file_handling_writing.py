from datetime import datetime

now = datetime.now()
formatted_time = now.strftime("%d %B %Y, %H:%M:%S")
print(formatted_time)

""" with open('notes.txt', 'a') as f:
    f.write(f'{formatted_time} - Asab - creating on the platform\n') """
# f.write('You live in Helsink')


with open('logs.txt', 'a') as f:
        f.write(f'{formatted_time} - John - creating a bucket\n')