import uuid
import hashlib
import getpass

class User:

    users_dict = {}

    def __init__(self,user_name,password,phone_number,id):
        self.__password = password
        self.username = user_name
        self.phonenumber = phone_number
        self.id= id

    @classmethod
    def get_info(cls,name,passwd,phone):
        SpecialSym =['$', '@', '#', '%']
        
        if name != '' and name not in cls.users_dict:
            cls.username = name
        else:
            return print('Error name value is empty or Its already exists')
        if len(passwd) < 6:
            return print('length should be at least 6')
            
         
        if len(passwd) > 20:
            return print('length should be not be greater than 8')
            
         
        if not any(char.isdigit() for char in passwd):
            return print('Password should have at least one numeral')
            
         
        if not any(char.isupper() for char in passwd):
            return print('Password should have at least one uppercase letter')
            
         
        if not any(char.islower() for char in passwd):
            return print('Password should have at least one lowercase letter')
            
         
        if not any(char in SpecialSym for char in passwd):
            return print('Password should have at least one of the symbols $@#')
            
        cls.__password = passwd
        
        if phone == '':
            cls.phonenumber = None
        else:
            cls.phonenumber = phone
        cls.id = str(uuid.uuid5(uuid.NAMESPACE_DNS,name))
        
        cls.users_dict[name] = [hashlib.sha256(passwd.encode('utf-8')).hexdigest(),phone,str(uuid.uuid5(uuid.NAMESPACE_DNS,name))]

    @classmethod
    def check_user_pass(cls,name,passwd):
        if name in cls.users_dict:
            if cls.users_dict[name][0] == hashlib.sha256(passwd.encode('utf-8')).hexdigest():
                return True
            else:
                return False
        return False
    
    @classmethod
    def print_user_info(cls,name):
        return f"your username:{name}\nyour phone number: {cls.users_dict[name][1]}\nyour Id = {cls.users_dict[name][2]}"
    
    @classmethod
    def rename(cls,prevusername,username,phone):
        
        if username not in cls.users_dict:
            cls.users_dict[username] = cls.users_dict.pop(prevusername)
            print('username and id changed')
            if phone == '':
                pass
            else:
                cls.users_dict[username][1] = phone
        else:
            print('username is already exist')
        

    @staticmethod
    def changepassword(username,prev_pass,passwd,confirm_new_pass):
        
        SpecialSym =['$', '@', '#', '%']
        
        if len(passwd) < 6:
            return print('length should be at least 6')
            
         
        if len(passwd) > 20:
            return print('length should be not be greater than 8')
            
         
        if not any(char.isdigit() for char in passwd):
            return print('Password should have at least one numeral')
            
         
        if not any(char.isupper() for char in passwd):
            return print('Password should have at least one uppercase letter')
            
         
        if not any(char.islower() for char in passwd):
            return print('Password should have at least one lowercase letter')
            
         
        if not any(char in SpecialSym for char in passwd):
            return print('Password should have at least one of the symbols $@#')
            
        if User.users_dict[username][0] == hashlib.sha256(prev_pass.encode('utf-8')).hexdigest():
            if passwd == confirm_new_pass:
                User.users_dict[username][0] = hashlib.sha256(passwd.encode('utf-8')).hexdigest()
            else:
                print('new_password not match with confirm')
        else:
            print('last password is not correct')
        print('password was changed')

while True:

    operaton = input("enter 0 for Exit and 1 for signup 2 for sigh in : ")
    
    if operaton == '1':
        info_username = input("enter Username please: ")
        info_password = getpass.getpass('enter password please: ')
        phone_number = input("please enter your phone number(optional): ")
        User.get_info(info_username,info_password,phone_number)

    elif operaton == '2':
        username = input('enter username for log in please: ')
        password = getpass.getpass('enter password please: ')
        operaton_2 =  User.check_user_pass(username,password)

        if operaton_2 == True:
            operaton_3 = input('1 for print info 2 for rename 3 for change password 4 for back to menu: ')

            if operaton_3 == '1':
                print(User.print_user_info(username))
                
            elif operaton_3 == '2':
                new_username = input("enter your new username: ")
                phone = input("please enter your phone number(optional): ")
                User.rename(username,new_username,phone)

            elif operaton_3 == '3':
                last_password = getpass.getpass('enter your last password please: ')
                new_password = getpass.getpass('enter your new password please: ')
                conferm_new_password = getpass.getpass('confirm your password please: ')
                User.changepassword(username,last_password,new_password,conferm_new_password)

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