# Date detection validation using regex
# DD/MM/YYYY format
import re

# date_regex = re.compile(r'\d{2}/\d{2}/\d{4}')
date_regex = re.compile(r'([0-3][0-9])/([0-1][0-9])/([0-2][0-9][0-9][0-9])')

def is_leap_year(year):
    if int(year) % 4 == 0 and int(year) % 100 != 0:
        return "is leap year"
    elif int(year) % 4 == 0 and int(year) % 100 == 0:
        if int(year) % 400 == 0:
            return "is leap year"
        else:
            return "is not leap year"
    else:
        return "is not leap year"

def date_detection(date):
    month_thirty = (4, 6, 9, 11)
    month_thirty_one = (1, 3, 5, 7, 8, 10, 12)
    try:
        split_date = date_regex.search(date)
        day, month, year = split_date.groups()
    except:
        return "invalid date"
    if int(month) in month_thirty and int(day) <= 30:
        return "valid date"
    elif int(month) in month_thirty_one and int(day) <= 31:
        return "valid date"
    elif int(month) == 2 and is_leap_year(year) == "is leap year":
        if int(day) <= 29:
            return "valid date"
        else:
            return "invalid date"
    elif int(month) == 2 and is_leap_year(year) == "is not leap year":
        if int(day) <= 28:
            return "valid date"
        else:
            return "invalid date"
    else:
        return "invalid date"

date_detection('01/01/1000') # valid date
date_detection('13/04/2029') # valid date
date_detection('01/01/3000') # invalid date
date_detection('40/01/1999') # invalid date
date_detection('01/13/1999') # invalid date