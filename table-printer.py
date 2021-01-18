# table-printer.py

table_data = [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']]

def print_table(table):
    columns = []
    for stuffs in range(len(table)):
        longest_word = ''
        # Find the longest word in each list
        for word in table[stuffs]:
            if len(word) > len(longest_word):
                longest_word = word
            else:
                longest_word = longest_word
        columns.append(len(longest_word))
    # Loop through the table and columns list and print out each word with it's required justification
    for stuffs in range(len(table_data[0])):
        for length in range(len(columns)):
            print(table_data[length][stuffs].rjust(columns[length]), end=' ')
        print()

print_table(table_data)

