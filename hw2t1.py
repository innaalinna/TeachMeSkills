import calendar as c
from datetime import datetime as dt
print("Please enter date in format DD.MM.YYYY: ")

while True:
    try:
        dateBirthStr = str(input())
        dateBirth = dt.strptime(dateBirthStr, '%d.%m.%Y')
    except ValueError as e:
        print(e)
    else:
        break

print("Week day of date is: "+str(c.day_name[c.weekday(dateBirth.year, dateBirth.month, dateBirth.day)]))

