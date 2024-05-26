number = int(input("please enter the number: "))

Divisor_sum = 0

for x in range(1,number):
    if number % x == 0:
        Divisor_sum += x

if Divisor_sum == number:
    print('Yes')
    
else:
    print('No')