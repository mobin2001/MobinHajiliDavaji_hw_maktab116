import re

def Capital_space(letter):
    capital_string_list = []
    capital_string_list = re.findall('[A-Z][^A-Z]*', Entrance)
    capital_space_string = ''

    for item in capital_string_list:
        capital_space_string += item + ' '

    print(capital_space_string[:-1])

Entrance = input()

Capital_space(Entrance)