class User:

    Id = 0

    users_dict = {}

    def __init__(self,user_name,password,phone_number):
        self.__password = password
        self.username = user_name
        self.phonenumber = phone_number

    @classmethod
    def get_info(cls,name,passw,phone):
        if name != '':
            cls.username = name
        else:
            print('error name value is empty')
        if len(passw) >= 4:
            cls.__password = passw
        else:
            return print('error password must be at least 5 characters')
        if phone == '':
            cls.phonenumber = None
        else:
            cls.phonenumber = phone
        cls.users_dict[name] = [passw,phone,cls.Id + 1]

    @classmethod
    def check_user_pass(cls,name,pasw):
        if name in cls.users_dict:
            if cls.users_dict[name][0] == pasw:
                return True
            else:
                return False
        return False
    
    @classmethod
    def print_user_info(cls,name):
        return (name,cls.users_dict[name][1] , cls.users_dict[name][2]).__str__()
    
    @classmethod
    def rename(cls,prevusername,username,phone):
        
        if username not in cls.users_dict:
            cls.users_dict[username] = cls.users_dict.pop(prevusername)
            cls.users_dict[username][1] = phone
        else:
            print('username is not confirmed')

    @staticmethod
    def changepassword(username,prev_pass,new_pass,confirm_new_pass):
        if User.users_dict[username][0] == prev_pass:
            if new_pass == confirm_new_pass:
                User.users_dict[username][0] = new_pass
            else:
                print('new_password not match with confirm')
        else:
            print('last password is not correct')
        

while True:
    operaton = input("enter 0 for Exit and 1 for signup 2 for sigh in : ")
    if operaton == '1':
        info = input("enter Username and passpord please(password at least 4 char): ").split()
        phone_number = input("please enter your phone number: ")
        User.get_info(info[0],info[1],phone_number)

    elif operaton == '2':
        user_info = input('enter username and password for sigh in: ').split()
        operaton_2 =  User.check_user_pass(user_info[0],user_info[1])

        if operaton_2 == True:
            operaton_3 = input('1 for print info 2 for rename 3 for change password 4 for back to menu: ')

            if operaton_3 == '1':
                print(User.print_user_info(user_info[0]))
                
            elif operaton_3 == '2':
                new_info = input("enter your new username and phonenumber: ").split()
                User.rename(info[0],new_info[0],new_info[1])

            elif operaton_3 == '3':
                last_password = input("enter your last password: ")
                new_password = input("enter new pass:")
                conferm_new_password = input("confirm password: ")
                User.changepassword(user_info[0],last_password,new_password,conferm_new_password)

            elif operaton_3 == '4':
                pass

            else:
                print('wrong operation!!!')

        else:
            print('invalid username or password')

    elif operaton == '0':
        break

    elif operaton != '1' or operaton != '0':
        print('wrong input!!!')

