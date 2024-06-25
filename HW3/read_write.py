import csv
import logging

def sed(input_file_name, output_file_name,pattern_string,replacemetn_string):

    csv_reader = None

    try:
        with open(input_file_name, 'r', newline = '') as fin:

            csv_reader = fin.read()

            with open(output_file_name, 'w', newline='') as fout:


                if pattern_string in csv_reader:
                    csv_reader = csv_reader.replace(pattern_string,replacemetn_string)

                fout.write(csv_reader)
                fout.close
                #fout.write('\n')

    except IOError:
        logging.exception('')

    if not csv_reader:
        raise ValueError('No data available')

sed('E:/python/input.csv','E:/HW/HW3/output.csv','mandana','maryam')