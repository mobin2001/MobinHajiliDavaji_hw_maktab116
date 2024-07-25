import auth
import getpass

class User(auth.Authenticator):

    def __init__(self):

        super().__init__()
        self.is_logged_in = False
        self.username = ''
        self.__password = ''

u1 = User()
u1.add_user(input('Please enter username for sign up: '),getpass.getpass('Please enter password(at least 8 char): '))
u1.login(input('Enter your username for log in: '),getpass.getpass('Enter your password: '))
u1.is_logged_inn()

u2 = User()
u2.add_user(input('Please enter username for sign up: '),getpass.getpass('Please enter password(at least 8 char): '))
u2.is_logged_inn()

# while True:
#     operation = input('Please enter 1 for sign up 2 for login and 0 for Exit: ')
#     if operation == '1':
#         User.add_user(input('Please enter username for sign up: '),getpass.getpass('Please enter password(at least 8 char): '))
#     elif operation == '2':
#         User.login(input('Enter your username for log in: '),getpass.getpass('Enter your password: '))
#     elif operation != '1' or operation != '2' or operation != '0':
#         print('wrong operation')
#     elif operation == '0':
#         break