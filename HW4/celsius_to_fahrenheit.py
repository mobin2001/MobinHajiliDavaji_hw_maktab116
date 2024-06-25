def c_to_f(celisius):
    fahrenheit = (celisius * (9 / 5)) + 32
    return fahrenheit

my_list = [8,2,3,-1,7]

list_fahrenheit = list(map(c_to_f,my_list))

print(list_fahrenheit)