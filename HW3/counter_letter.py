my_string = input()

dict_counter = dict()

for letter in my_string:

    dict_counter[letter] = dict_counter.get(letter, 0) + 1

print(dict_counter)