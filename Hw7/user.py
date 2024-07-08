import auth

class User(auth.Authenticator):

    def __init__(self):

        super().__init__()
        self.is_logged_in = False
        self.username = ''
        self.__password = ''

u1 = User()
u1.add_user('mobin','A1234567')
u1.login('mobin','A1234567')
u1.is_logged_inn()