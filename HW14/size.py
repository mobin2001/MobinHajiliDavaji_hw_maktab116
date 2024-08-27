import os
import argparse

def get_dir_size(path):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


def get_file_size(path):
    total = 0

    total += os.path.getsize(path)
              
    print(f'file sizes : {total}')


def get_file_size_with_type(path,type):
    total = 0
    for file in os.listdir(path):
	# check the files which are end with specific extension
        if file.endswith(type):
            total += os.path.getsize(f'{path}/{file}')
              
    print(f'file sizes with {type}: {total / 1024} kb')

parser = argparse.ArgumentParser(description='Calculate the size of a directory or file in kilobytes (KB).')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-d', '--directory', type=str, help='Directory path to calculate size of.')
group.add_argument('-f', '--file', type=str, help='File path to calculate size of.')
parser.add_argument('-F', '--filter', type=str, help='Filter files by extension (e.g., pdf, txt). Used only with -d.')

args = parser.parse_args()

try:
    if args.filter:
        get_file_size_with_type(args.directory,args.filter)
    elif args.directory:
        size = get_dir_size(args.directory)
        print(f"Total size of '{args.directory}' is {size / 1024} KB.")
    elif args.file:
        if not os.path.isfile(args.file):
            raise FileNotFoundError(f"The file '{args.file}' does not exist.")
        size = os.path.getsize(args.file) / 1024
        print(f"Size of file '{args.file}' is {size:.2f} KB.")
    
# except FileNotFoundError as e:
#     print(e)
except BaseException as e:
    print(f"An unexpected error occurred: {e}")