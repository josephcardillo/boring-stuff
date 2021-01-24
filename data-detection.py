# Date detection validation using regex
# DD/MM/YYYY format
import re

# date_regex = re.compile(r'\d{2}/\d{2}/\d{4}')
date_regex = re.compile(r'([0-3][0-9])/([0-1][0-9])/([0-2][0-9][0-9][0-9])')

def is_leap_year(year):
    if int(year) % 4 == 0 and int(year) >= 100:
        if int(year) % 100 == 0 and int(year) % 400 == 0:
            return "is leap year"
        elif int(year) % 100 == 0 and not int(year) % 400 == 0:
            return "is not leap year"
    elif int(year) % 4 == 0:
        return "is leap year"
    else:
        return "is not leap year"

def date_detection(date):
    split_date = date_regex.search(date)
    day, month, year = split_date.groups()
    if int(month) in (4, 6, 9, 11) and int(day) <= 30:
        return "valid date"
    elif int(month) in 2 and int(day) <= 29:
        # TODO - incorporate is_leap_year function
    else:
        return "invalid date"