#! /usr/bin/python3

# Strong Password Detection
# Automate the Boring Stuff - Ch. 7 Exercise

import re

pw_regex_lowercase = re.compile(r'[a-z]+')
pw_regex_uppercase = re.compile(r'[A-Z]+')
pw_regex_digit = re.compile(r'[0-9]+')

# password = input('Enter your password > ')

def strong_password(password):
    if len(password) < 8:
        return 'Invalid password.'
    elif len(password) >= 8:
        validate_lowercase = pw_regex_lowercase.search(password)
        validate_uppercase = pw_regex_uppercase.search(password)
        validate_digit = pw_regex_digit.search(password)
    try:
        validate_lowercase.group()
        validate_uppercase.group()
        validate_digit.group()
        return 'Valid password'
    except:
        return 'Invalid password.'



print(strong_password('12345')) # Invalid password.
print(strong_password('abcdefghi')) # Invalid password.
print(strong_password('gHgHgHgHgH')) # Invalid password.
print(strong_password('45greatandGood')) # Valid password.
print(strong_password('TomorrowAfternoon123')) # Valid password