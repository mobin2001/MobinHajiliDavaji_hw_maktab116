import exceptions
import hashlib



class Authenticator:

    users = {}

    def __init__(self):
        pass
        
    def add_user(self,name,passwd):
        
        if name != '' and name not in self.users:

            self.username = name
        else:

            raise exceptions.UsernameAlreadyExists()
        
        if len(passwd) < 8:

            raise exceptions.PasswordTooShort()
        
        else:

            self.__password = passwd

        self.users[name] = hashlib.sha256(passwd.encode('utf-8')).hexdigest()

    
    def login(self,name,passwd):

        if name in self.users:

            if self.users[name] == hashlib.sha256(passwd.encode('utf-8')).hexdigest():

                print('User logged in')
                self.is_logged_in = True
                
            
            else:

                raise exceptions.InvalidPassword()
        else:
            raise exceptions.InvalidUsername()
        

    def is_logged_inn(self):

        if self.is_logged_in == True:

            print('user is loged in')

        else:

            print('user is not log in')
    
