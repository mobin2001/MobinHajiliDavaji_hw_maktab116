import argparse
import pickle
from typing import Dict
from pathlib import Path
from datetime import datetime
from functools import wraps


class InvalidAccountNumber(BaseException):
    def __str__(self) -> str:
        return "invalid acount number(account number should be 12 char)"


class InvalidCardNumber(BaseException):
    def __str__(self) -> str:
        return "invalid acount number(account number should be 16 char)"


class AccountNumberDontExist(BaseException):
    def __str__(self) -> str:
        return "this account number dosen't exist in data"


class InvalidBankNameException(BaseException):
    def __str__(self) -> str:
        return "Bank name is  incorrect"


class InvalidAmountException(BaseException):
    def __str__(self) -> str:
        return "Invalid amount(amount most be postive number)"


class AccountNaumberIsAlreadyExistException(BaseException):
    def __str__(self) -> str:
        return "Account number is already exist"


class InsufficientInventoryException(BaseException):
    def __str__(self) -> str:
        return "Insufficient inventory"


class NoDataException(BaseException):
    def __str__(self) -> str:
        return "No date in file"


def log_decorator(func):
    
    def wrapper(*args, **kwargs):
        log_time = datetime.now()
        result = func(*args, **kwargs)
        with open(
            "/home/mobin/HW/MobinHajiliDavaji_hw_maktab116/HW8/log_file.txt", "a"
        ) as log_file:
            log_file.write(f"log time:{log_time} operation : {func.__name__}\n")

    return wrapper


class AccountManagement:

    ـobjects: Dict[str, "AccountManagement"] = {}

    def __init__(
        self, bank_name: str, account_number: str, card_number: str, amount: int
    ) -> None:
        self.bank_name = bank_name
        self.account_number = account_number
        self.card_number = card_number
        self.amount = amount
        self.transaction: Dict[str, int] = {}
        self.frequent_transactions: Dict[str, int] = {}  # type: ignore

        AccountManagement.ـobjects[account_number] = self  # type: ignore
        AccountManagement.save(account_number)

    @classmethod
    @log_decorator
    def save(cls, account_number: str) -> None:
        myfile = Path("/home/mobin/HW/MobinHajiliDavaji_hw_maktab116/HW8/accounts")
        if myfile.is_file():
            with open(
                "/home/mobin/HW/MobinHajiliDavaji_hw_maktab116/HW8/accounts", "rb"
            ) as fin:
                data = pickle.load(fin)
                if account_number not in data:
                    data.update(AccountManagement.ـobjects)
                    with open(
                        "/home/mobin/HW/MobinHajiliDavaji_hw_maktab116/HW8/accounts",
                        "+wb",
                    ) as fout:
                        pickle.dump(data, fout)
                        print("account created")
                        fout.close
                else:
                    raise AccountNaumberIsAlreadyExistException
        else:
            with open(
                "/home/mobin/HW/MobinHajiliDavaji_hw_maktab116/HW8/accounts", "+wb"
            ) as fout:
                pickle.dump(AccountManagement.ـobjects, fout)
                print("account created")
                fout.close

    @classmethod
    def get(cls, account_number: str):

        with open(
            "/home/mobin/HW/MobinHajiliDavaji_hw_maktab116/HW8/accounts", "rb"
        ) as fin:
            data = pickle.load(fin)
            if account_number in data:
                return data[account_number]
            else:
                AccountNumberDontExist

    @classmethod
    @log_decorator
    def add_income(cls, account_number: str, income_amount: int) -> None:
        account = AccountManagement.get(account_number)
        account.amount = account.amount + income_amount
        transaction_type = input("please enter transction type: ")
        account.transaction[transaction_type] = income_amount
        operation = input("do you want to add this transction to frequent?(yes,no)")
        if operation == "yes":
            account.frequent_transactions[f"{transaction_type}_income"] = income_amount
        with open(
            "/home/mobin/HW/MobinHajiliDavaji_hw_maktab116/HW8/accounts", "rb"
        ) as fin:
            data = pickle.load(fin)
            data.pop(account_number)
            data.update({account_number: account})
            with open(
                "/home/mobin/HW/MobinHajiliDavaji_hw_maktab116/HW8/accounts", "wb"
            ) as fout:
                pickle.dump(data, fout)
        print(f"transaction completer your balance: {account.amount}")

    @classmethod
    @log_decorator
    def add_cost(cls, account_number: str, cost_amount: int) -> None:
        account = AccountManagement.get(account_number)
        if account.amount - cost_amount > 0:
            account.amount = account.amount - cost_amount
            transaction_type = input("please enter transction type: ")
            account.transaction[transaction_type] = -cost_amount
            operation = input("do you want to add this transction to frequent?(yes,no)")
            if operation == "yes":
                account.frequent_transactions[f"{transaction_type}_cost"] = -cost_amount
            with open(
                "/home/mobin/HW/MobinHajiliDavaji_hw_maktab116/HW8/accounts", "rb"
            ) as fin:
                data = pickle.load(fin)
                data.pop(account_number)
                data.update({account_number: account})
                with open(
                    "/home/mobin/HW/MobinHajiliDavaji_hw_maktab116/HW8/accounts", "wb"
                ) as fout:
                    pickle.dump(data, fout)
        else:
            raise InsufficientInventoryException
        print(f"transaction completer your balance: {account.amount}")

    @classmethod
    @log_decorator
    def frequent_transaction(cls, account_number: str) -> None:
        account = cls.get(account_number)
        with open(
            "/home/mobin/HW/MobinHajiliDavaji_hw_maktab116/HW8/accounts", "rb"
        ) as fin:
            data = pickle.load(fin)
            frequent_data = account.frequent_transactions
            l = 0
            for item in frequent_data:
                print(f"{l} = {item}: {frequent_data[item]}")
                l += 1

            choice = input(
                f"choose from list above or {l} for cancel operation and back to menu: "
            )
            if choice != str(l):
                amount = list(frequent_data.items())[int(choice)][1]
                if "cost" in list(frequent_data.items())[int(choice)][0]:
                    if account.amount + amount > 0:
                        account.amount += amount
                    else:
                        raise InsufficientInventoryException
                elif "income" in list(frequent_data.items())[int(choice)][0]:
                    account.amount += amount
                data.pop(account_number)
                data.update({account_number: account})
                with open(
                    "/home/mobin/HW/MobinHajiliDavaji_hw_maktab116/HW8/accounts", "wb"
                ) as fout:
                    pickle.dump(data, fout)
                print(f"transaction completer your balance: {account.amount}")
            else:
                None

    @classmethod
    def transactions(cls, account_number: str) -> None:
        account = AccountManagement.get(account_number)
        transactions = account.transaction
        l = 1
        for item in list(transactions.items()):
            print(f"{l}: {item}")
            l += 1

    def __str__(self) -> str:
        return f"Bank name: {self.bank_name}\nCard number: {self.card_number}\nAmount: {self.amount}"


def account_number_validation(account_number: str) -> str:
    if len(account_number) != 12 or not account_number.isdigit():
        raise InvalidAccountNumber
    return account_number


def card_number_validation(card_number: str) -> str:
    if len(card_number) != 16 or not card_number.isdigit():
        raise InvalidCardNumber
    return card_number


def bank_name_validation(bank_name: str) -> str:
    if len(bank_name) == 0 or len(bank_name) > 10:
        raise InvalidBankNameException
    return bank_name


def amount_validation(amount: str) -> int:
    if int(amount) < 0:
        raise InvalidAmountException
    return int(amount)


def argparser() -> "argparse.ArgumentParser":

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command")

    parser_detail = subparser.add_parser("account_details")
    parser_detail.add_argument("account_number", type=account_number_validation)

    add_accout_parser = subparser.add_parser("add_account")
    add_accout_parser.add_argument("bank_name", type=bank_name_validation)
    add_accout_parser.add_argument("account_number", type=account_number_validation)
    add_accout_parser.add_argument("card_number", type=card_number_validation)
    add_accout_parser.add_argument("amount", type=amount_validation)

    add_cost_parser = subparser.add_parser("add_cost")
    add_cost_parser.add_argument("account_number", type=account_number_validation)
    add_cost_parser.add_argument("amount", type=amount_validation)

    add_income_parser = subparser.add_parser("add_income")
    add_income_parser.add_argument("account_number", type=account_number_validation)
    add_income_parser.add_argument("amount", type=amount_validation)

    frequent_transaction_parser = subparser.add_parser("frequent")
    frequent_transaction_parser.add_argument(
        "account_number", type=account_number_validation
    )

    transaction_list_parser = subparser.add_parser("transaction_list")
    transaction_list_parser.add_argument(
        "account_number", type=account_number_validation
    )

    exit_parser = subparser.add_parser("exit")

    return parser


def main():

    while True:

        try:

            parser = argparser()
            args = parser.parse_args(input().split())
            command = args.command

            if command == "add_account":
                AccountManagement(
                    args.bank_name, args.account_number, args.card_number, args.amount
                )

            elif command == "add_cost":
                AccountManagement.add_cost(args.account_number, args.amount)

            elif command == "add_income":
                AccountManagement.add_income(args.account_number, args.amount)

            elif command == "account_details":
                print(AccountManagement.get(args.account_number))

            elif command == "frequent":
                AccountManagement.frequent_transaction(args.account_number)

            elif command == "transaction_list":
                AccountManagement.transactions(args.account_number)

            elif command == "exit":
                break

        except BaseException as e:
            log_time = datetime.now()
            print(e)
            with open(
                "/home/mobin/HW/MobinHajiliDavaji_hw_maktab116/HW8/log_file.txt", "a"
            ) as log_file:
                log_file.write(f"exception raise time:{log_time}\n")


if __name__ == "__main__":
    main()