def string_to_integer(list_string):

    list_of_numbers = list_string.split()

    for i in range(0,len(list_of_numbers)):
        list_of_numbers[i] = int(list_of_numbers[i])
        
    return list_of_numbers
    




n_m = input("please enter n(for numbers of set z) and m(for numbers setts a and b): ")
z_collection = input("z:")
A_collection = input("A:")
B_collection = input("B:")

z_list = string_to_integer(z_collection)
a_list = string_to_integer(A_collection)
b_list = string_to_integer(B_collection)

happy_count = 0

for item in a_list:

    if item in z_list:
        happy_count += 1

for item in b_list:
    
    if item in z_list:
        happy_count -= 1
        


print("happynes = ",happy_count)