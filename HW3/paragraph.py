import string
 
my_string = input()
 
my_string_punctuation = my_string.translate(str.maketrans('', '', string.punctuation))


list_of_paragraph = my_string_punctuation.lower().split()

dict_of_paragraph = dict.fromkeys(list_of_paragraph,0)

for item in list_of_paragraph:
    dict_of_paragraph[item] = dict_of_paragraph.get(item) + 1

list_three_top = list(dict_of_paragraph.items())

list_three_top.sort(key = lambda x: x[1], reverse= True)
print(list_three_top)
list_of_words = []
count = []

for x in range(3):
    list_of_words.append(list_three_top[x][0])
    count.append(list_three_top[x][1])
print('Most Frequent Word(s): ',list_of_words,'\nFrequence: ',count[0])




#This is a sample paragraph. It contains several words, some of which are repeated. This is a good exercise to find the most frequent words.