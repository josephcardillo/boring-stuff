# Regex version of the strip() method exercise
# Ch 7 - Automate the Boring Stuff

import re

def regex_strip_space(string, chars_to_remove=''):
    # IN PROGRESS
    if string[0] == ' ' and string[-1] != ' ':
        strip_space_regex = re.compile(f'^\s+')
        stripped_string = strip_space_regex.sub('', string)
        return stripped_string
    elif string[-1] == ' ' and string[0] != ' ':
        strip_space_regex = re.compile(f'(\w+)(\s+)')
        stripped_string = strip_space_regex.findall(string)[0][0]
        return stripped_string
    elif string[0] == ' ' and string[-1] == ' ':
        strip_space_regex = re.compile(f'(\s+)(\w+)(\s+)')
        stripped_string = strip_space_regex.findall(string)
        return stripped_string[0][1]
    elif chars_to_remove != '':
        strip_space_regex = re.compile(f'[{chars_to_remove}]')
        stripped_string = strip_space_regex.sub('', string)
        return stripped_string
    else:
        pass