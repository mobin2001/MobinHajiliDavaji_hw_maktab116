class Bankaccount:

    bank_accounts = {}

    def __init__(self,name,account_balance) -> None:
        self.name = name
        self.__minimum_account_balance = 50000
        if account_balance > self.__minimum_account_balance:
            self.account_balance = account_balance
        else:
            raise Exception(f'Account balance must be more than {self.__minimum_account_balance}')
        

    def harvest(self,amount):
        if amount > 0:
            if self.account_balance - amount > self.__minimum_account_balance:
                self.account_balance -= amount
                print(f'Successful operation\nYour account balance = {self.account_balance}')
            else:
                raise Exception(f'Account balance cant be less then {self.__minimum_account_balance}')
        else:
            raise Exception('Input amount number most be positive number')


    def deposit(self,amount):
        if amount > 0:
            self.account_balance += amount
            print(f'Successful operation\nYour account balance = {self.account_balance}')
        else:
            raise Exception('Input amount number most be positive number')

    def transfer(self,other,amount):
        if amount > 0:
            if self.account_balance - amount > self.__minimum_account_balance:
                self.account_balance -= amount
                other.account_balance += amount
                print(f'Successful operation\nYour account balance = {self.account_balance}')
            else:
                raise Exception(f'Account balance cant be less then {self.__minimum_account_balance}')
        else:
            raise Exception('Input amount number most be positive number')


    def display(self):
        print(f"Account name = {self.name}\nAccount balance = {self.account_balance}")

u1 = Bankaccount('Mobin',1000000)
u2 = Bankaccount('Nima',200000)

u1.harvest(200000)
u1.deposit(50000)


u1.transfer(u2,700000)
u1.display()
u2.display()