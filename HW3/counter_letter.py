my_string = 'www.google.com'

string_counter = dict()

for letter in my_string:

    string_counter[letter] = string_counter.get(letter, 0) + 1

print(string_counter)