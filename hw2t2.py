import calendar as c
from datetime import datetime as dt

print("Please enter week day: ")

weekDay = str(input())
weekDays = []
weekDays = c.day_name
while True:
    if weekDay not in weekDays:
        print("String is not a week day, please retype.")
        break
    else:
        break
currDate = dt.now()
year, month = currDate.year, currDate.month
while year <= currDate.year:

    if c.day_name[c.weekday(year, month, 1)] == weekDay:

        m = month
        break
    else:

        m = month
        while m in range(1, month + 1):
            if c.day_name[c.weekday(year, m, 1)] == weekDay:

                break
            else:

                m -= 1
        month = 12
        year -= 1
        break
print("Answer is: {:d}.{:d}.{:d}".format(1, m, year))
