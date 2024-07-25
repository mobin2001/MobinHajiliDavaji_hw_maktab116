import argparse
import csv

class AccountManagement:
    
    def __init__(self) -> None:
        pass

    @classmethod
    def add_account(cls,bank_name,amount,card_number,account_number):
        try:
            with open('bank_accounts.csv','r') as file:
                data = file.read()
                # print(type(data))
                if account_number not in data and card_number not in data:
                    with open('bank_accounts.csv','a') as fin:
                        fin.write(f'{bank_name},{amount},{card_number},{account_number}\n')
                file.close
        except:
            with open('bank_accounts.csv','a') as fin:
                fin.write(f'{bank_name},{amount},{card_number},{account_number}\n')
            fin.close
    @classmethod
    def casts(cls,amount):
        with open('costs.csv','a') as file:
            file.write(amount)
    @classmethod
    def transation(cls,account):
        pass
    @classmethod
    def income(cls,amount,category,account_number,frequent):
        if frequent:
            with open('frequent.csv','a') as file:
                file.write(f'{category},{amount},{account_number}')
    @classmethod
    def display(cls,account):
        with open('bank_accounts.csv','r') as fin:
            data = fin.readlines()
            print(type(data))
            print(data)
            for line in data:
                if account in line:
                    line = line[:-1].split(',')
                    return f'Bank: {line[0]}\nAmount: {line[1]}\nCard number: {line[2]}\nAccount number: {line[3]}'
            else:
                print('no data')
        

    


parser = argparse.ArgumentParser()
parser.add_argument('-o','--operation',required= True,choices=['add_account','add_cost','add_income','account_details','trancaions'])
parser.add_argument('-a','--account_number',required=True)
parser.add_argument('-b','--bank_name',required=False)
parser.add_argument('-c','--card_number',required=False)
parser.add_argument('-A','--Amount',required=False)
parser.add_argument('-i','--income_category',required=False,choices=['salary','profit','inheritance'])
parser.add_argument('-r','--repetitive',action='store_true',default=False)
args = parser.parse_args()
if args.operation == 'add_account':
    AccountManagement.add_account(args.bank_name,args.Amount,args.card_number,args.account_number)
elif args.operation == 'account_details':
    print(AccountManagement.display(args.account_number))
elif args.operation == "add_income":
    AccountManagement.income(args.amount,args.income_category,args.account_number,args.repetitive)