#! python3
# pig-latin.py - pig latin translator

import pyperclip

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

message = input('Enter the English message to translate into Pig Latin: ')

pig_latin = []
for word in message.split():
    prefix_non_letters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]
    if len(word) == 0:
        pig_latin.append(prefix_non_letters)
        continue

    suffix_non_letters = ''
    while not word[-1].isalpha():
        suffix_non_letters += word[-1]
        word = word[:-1]

    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower()

    prefix_consonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]

    if prefix_consonants != '':
        word+= prefix_consonants + 'ay'
    else:
        word += 'yay'

    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()

    pig_latin.append(prefix_non_letters + word + suffix_non_letters)

print(' '.join(pig_latin))