import csv
import logging

def sed(input_file_name, output_file_name,pattern_string,replacemetn_string):
    csv_reader = None
    try:
        with open(input_file_name, 'r', newline = '') as fin:

            csv_reader = fin.read()

            with open(output_file_name, 'w', newline='') as fout:

                # for item in csv_reader:

                #     row = ''
                #     print(item)
                #     for x in range(len(item)):

                #         row += item
                #         row += ','
                #         if pattern_string in row:
                #             row.replace(pattern_string,replacemetn_string)

                #     fout.writelines(row[:-1])
                if pattern_string in csv_reader:
                    csv_reader = csv_reader.replace(pattern_string,replacemetn_string)

                fout.write(csv_reader)
                fout.close
                #fout.write('\n')
    except IOError:
        logging.exception('')   #UnicodeDecodeError
    if not csv_reader:
        raise ValueError('No data available')

        

sed('E:/python/input.csv','E:/python/averages.csv','5','10')