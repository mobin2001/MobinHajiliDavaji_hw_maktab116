import string
 
def find_most_frequent_words(input_paragraph):
    my_string_punctuation = input_paragraph.translate(str.maketrans('', '', string.punctuation))
    list_of_paragraph = my_string_punctuation.lower().split()

    dict_of_paragraph = dict.fromkeys(list_of_paragraph,0)

    for item in list_of_paragraph:
        dict_of_paragraph[item] = dict_of_paragraph.get(item) + 1

    list_three_top = list(dict_of_paragraph.items())

    list_three_top.sort(key = lambda x: x[1], reverse= True)
    
    list_of_frequent_words = []
    count = []

    for x in range(3):
        list_of_frequent_words.append(list_three_top[x][0])
        count.append(list_three_top[x][1])
    return list_of_frequent_words,count[0]



my_string = 'This is a sample paragraph. It contains several words, some of which are repeated. This is a good exercise to find the most frequent words.'
 

list_of_words , counter = find_most_frequent_words(my_string)

print('Most Frequent Word(s): ',list_of_words,'\nFrequence: ',counter)

#This is a sample paragraph. It contains several words, some of which are repeated. This is a good exercise to find the most frequent words.