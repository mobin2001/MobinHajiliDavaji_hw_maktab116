def armstrong(x):
    yield x ** 3

my_num = '152'

sum = 0

for string in my_num:
    sum += next(armstrong(int(string)))
    
if sum == int(my_num):
    print('Armstrong')
else:
    print('not Armstrong')