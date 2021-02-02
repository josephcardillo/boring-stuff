# Regex version of the strip() method exercise
# Ch 7 - Automate the Boring Stuff

import re

def regex_strip_space(string, chars_to_remove=''):
    # IN PROGRESS
    strip_space_regex = re.compile(f'(\s+)(\w+)([{chars_to_remove}])(\s+)')
    stripped_string = strip_space_regex.findall(string)[0][1]
    return stripped_string

