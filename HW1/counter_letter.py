Entrance = input()

count_digits = 0
count_letters = 0

for letter in Entrance:
    if letter.isalpha():
        count_letters += 1
    elif letter.isnumeric():
        count_digits += 1

print('Letters: %s \nDigits: %s' %(count_letters,count_digits))