spam = ['apples', 'bananas', 'tofu', 'cats']
spam1 = ['apples', 'bananas', 'tofu', 'cats', 'oranges', 3]
spam2 = ['apples', 'bananas', 'tofu', 'cats', 2, 3]
spam3 = []
spam4 = ['apples']
spam5 = [5]

def sentence(words):
    if len(words) == 0:
        print("Your list is empty.")
    elif len(words) == 1:
        print(words[0])
    else:
        for word in words:
            if words.index(word) < (len(words) - 1):
                print(f"{str(word).strip()},", end=' ')
            else:
                print(f"and {word}")



# Alternate version:

def sentence(words):
    if len(words) == 0:
        return "Your list is empty."
    elif len(words) == 1:
        return "{}".format(str(words[0]))
    else:
        words_string = list(map(str, words))
        # print(a)
        return "{}, and {}".format(", ".join(words_string[:-1]), (words_string[-1]))


sentence(spam)
sentence(spam1)
sentence(spam2)
sentence(spam3)
sentence(spam4)
sentence(spam5)