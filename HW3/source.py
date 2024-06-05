import csv
from os import close
from statistics import mean 
from collections import Counter
import operator


def calculate_averages(input_file_name, output_file_name):
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
        sorted_dict = {}
        sorted_keys = sorted(avrage,key = avrage.get)

        for w in sorted_keys:
            sorted_dict[w] = avrage[w]
        sorted_dicts = list(sorted_dict.items())
        
        for x in range (0,len(sorted_dicts)-1):
            
            if sorted_dicts[x][1] == sorted_dicts[x+1][1]:
                print(sorted_dicts[x])
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
        avrage = dict()
        reader = csv.reader(fin)
        for row in reader:
            name = row[0]
            nomarat = list()
            for item in row[1:]:
                nomarat.append(float(item))
                nomarat = sorted(nomarat)
                avrage[name] = mean(nomarat)
        javab = [0,0,0]
        for x in range(0,3):
            minn = min(avrage, key=avrage.get)
            javab[x] = avrage[minn]
            avrage.pop(minn)
        with open(output_file_name, 'w', newline='') as fout:
            writer = csv.writer(fout)
            writer.writerows(map(lambda x: [x], javab))
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
        javab = [0]
        javab[0] = mean(avrage.values())
        with open(output_file_name, 'w', newline='') as fout:
            writer = csv.writer(fout)
            writer.writerows(map(lambda x: [x], javab))
            fout.close()
calculate_average_of_averages('E:/python/grades.csv','E:/python/average_averages.csv')