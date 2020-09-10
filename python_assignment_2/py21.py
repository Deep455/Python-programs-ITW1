import random
import datetime

datetime.datetime.strptime("2013-1-25", '%Y-%m-%d').strftime('%d/%m/%Y')
a = input("enter a starting date (in dd-mm-yyyy format) : ").split("-")
b = input("enter a ending date (in dd-mm-yyyy format) : ").split("-")
for i in range(3):
    a[i] = int(a[i])
    b[i] = int(b[i])

x = datetime.date(a[2], a[1], a[0])
y = datetime.date(b[2], b[1], b[0])

time_between_dates = y - x
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = x + datetime.timedelta(days=random_number_of_days)

z = str(random_date)
z = z.split("-")
print(z)
temp = z[2] + "-" + z[1] + "-" + z[0]
print(temp)