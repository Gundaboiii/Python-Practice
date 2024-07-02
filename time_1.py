import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp_hour = int(time.strftime('%H'))
print(timestamp_hour)
timestamp_minutes = time.strftime('%M')
print(timestamp_minutes)
timestamp_seconds = time.strftime('%S')
print(timestamp_seconds)
if timestamp_hour>0 & timestamp_hour<8:
    print("Good Night Sir")
elif timestamp_hour>8 & timestamp_hour<16:
    print("Good Morning Sir")
else:
    print("Good Evening Sir")