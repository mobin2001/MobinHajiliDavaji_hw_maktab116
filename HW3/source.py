import csv
from os import close
from statistics import mean 
from collections import Counter
import operator
from collections import OrderedDict

def write_in(input_file_name):

    with open('E:/python/grades.csv', 'w') as fout:

        data = '''mandana,5,7,3,15
hamid,3,9,4,20,9,1,8,16,0,5,2,4,7,2,1
sina,19,10,19,6,8,14,3
sara,0,5,20,14
soheila,13,2,5,1,3,10,12,4,13,17,7,7
ali,1,9
sarvin,0,16,16,13,19,2,17,8'''

        list_data = data.split('\n')
        
        for item in list_data:

            fout.write(item+'\n',)

        fout.close

write_in('E:/python/grades.csv')

def calculate_averages(input_file_name, output_file_name):

    with open(input_file_name, newline = '') as fin:

        avrage = OrderedDict()
        reader = csv.reader(fin)
        
        for row in reader:
            
            name = row[0]
            nomarat = list()

            for item in row[1:]:

                nomarat.append(float(item))
                nomarat = sorted(nomarat)
                avrage[name] = mean(nomarat)

        javabb = list(avrage.items())
        
        with open(output_file_name, 'w', newline='') as fout:

            writer = csv.writer(fout)
            writer.writerows(javabb)
            fout.close

calculate_averages('E:/python/grades.csv','E:/python/averages.csv')

def calculate_sorted_averages(input_file_name, output_file_name):

    with open(input_file_name, newline = '') as fin:

        avrage = dict()
        reader = csv.reader(fin)

        for row in reader:
            name = row[0]
            nomarat = list()

            for item in row[1:]:
                nomarat.append(float(item))
                nomarat = sorted(nomarat)
                avrage[name] = mean(nomarat)

        sorted_dict = OrderedDict()
        sorted_keys = sorted(avrage,key = avrage.get)
        
        for w in sorted_keys:

            sorted_dict[w] = avrage[w]
        sorted_dict
        sorted_dicts = list(sorted_dict.items())
        
        for x in range (0,len(sorted_dicts)-1):
            
            if sorted_dicts[x][1] == sorted_dicts[x+1][1]:

                if sorted_dicts[-2] == sorted_dicts[x]:
                    sortt = sorted(sorted_dicts[x:], key=lambda x: (x[0]))
                    del sorted_dicts[x:x+2]
                    sorted_dicts.insert(x,sortt[1])
                    sorted_dicts.insert(x,sortt[0])

                else:
                    sortt = sorted(sorted_dicts[x:x+2], key=lambda x: (x[0]))
                    del sorted_dicts[x:x+2]
                    sorted_dicts.insert(x,sortt[1])
                    sorted_dicts.insert(x,sortt[0])
        
        with open(output_file_name, 'w', newline='') as fout:

            writer = csv.writer(fout)
            writer.writerows(sorted_dicts)
            fout.close

calculate_sorted_averages('E:/python/grades.csv','E:/python/sorted_averages.csv')

def calculate_three_best(input_file_name, output_file_name):

    with open(input_file_name, newline = '') as fin:

        avrage = dict()
        reader = csv.reader(fin)

        for row in reader:
            name = row[0]
            nomarat = list()

            for item in row[1:]:
                nomarat.append(float(item))
                nomarat = sorted(nomarat)
                avrage[name] = mean(nomarat)

        k = Counter(avrage)
        print(k)
        high = list(k.most_common(3))
        
        if high[0][1] == high[1][1]:
            x = high.pop()
            high = sorted(high, key=operator.itemgetter(0))
            high.append(x)

        elif high[1][1] == high[2][1]:

            sorted_high = sorted(high[1:3], key=lambda x: (x[0]))
            del high[1:]
            high.append(sorted_high[0])
            high.append(sorted_high[1])
        
        with open(output_file_name, 'w', newline='') as fout:

            writer = csv.writer(fout)
            writer.writerows(high)
            fout.close

calculate_three_best('E:/python/grades.csv','E:/python/best_averages.csv')

def calculate_three_worst(input_file_name, output_file_name):
    
    with open(input_file_name, newline = '') as fin:

        reader = csv.reader(fin)
        average_nomarat = list()

        for row in reader:

            nomarat = list()

            for item in row[1:]:

                nomarat.append(float(item))
            average_nomarat.append(mean(nomarat))

        average_nomarat.sort()
            
        with open(output_file_name, 'w', newline='') as fout:

            writer = csv.writer(fout)
            for x in range(3):
                writer.writerow([average_nomarat[x]])
            fout.close()

calculate_three_worst('E:/python/grades.csv','E:/python/worst_averages.csv')

def calculate_average_of_averages(input_file_name, output_file_name):

    with open(input_file_name, newline = '') as fin:

        avrage = dict()
        reader = csv.reader(fin)

        for row in reader:
            name = row[0]
            nomarat = list()

            for item in row[1:]:

                nomarat.append(float(item))
                nomarat = sorted(nomarat)
                avrage[name] = mean(nomarat)

        
        javab = [mean(avrage.values())]

        with open(output_file_name, 'w', newline='') as fout:

            writer = csv.writer(fout)
            writer.writerows(map(lambda x: [x], javab))
            fout.close()

calculate_average_of_averages('E:/python/grades.csv','E:/python/average_averages.csv')