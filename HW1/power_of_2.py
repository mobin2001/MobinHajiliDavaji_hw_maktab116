number = int(input())

power_of_2 = ''

x = 1

while power_of_2 == '':
    power_2 = 2 ** x
    if number >= power_2:
        if number == power_2:
            power_of_2 = 'Yes'
        elif number > power_2:
            x += 1
    elif power_2 > number:
        power_of_2 = 'No'
    

print(power_of_2)