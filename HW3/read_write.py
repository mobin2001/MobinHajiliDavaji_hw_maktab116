import csv

def read_and_write(input_file_name, output_file_name,pattern_string,replacemetn_string):

    with open(input_file_name, newline = '') as fin:

        csv_reader = csv.reader(fin)
        
        list_data = list()

        for row in csv_reader:
            
            list_data.append(row)

        with open(output_file_name, 'w', newline='') as fout:

            for item in list_data:

                row = ''

                for x in range(len(item)):

                    if pattern_string != item[x]:
                        row += item[x]
                        row += ','

                    elif pattern_string == item[x]:

                        
                        row += item[x].replace(item[x],replacemetn_string)
                        row += ','

                fout.write(row[:-1])
                fout.write('\n')

            fout.close

read_and_write('E:/python/gradess.csv','E:/python/averages.csv','mandana','maryam')