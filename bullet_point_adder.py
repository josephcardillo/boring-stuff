#! python3
# bullet_point_adder.py - add bullet point and space before each item in a list

import pyperclip

list_of_lists = pyperclip.paste()
split_list = list_of_lists.split('\n')

for i in range(len(split_list)):
    split_list[i] = '* ' + split_list[i]

split_list = '\n'.join(split_list)
print(split_list)
pyperclip.copy(split_list)