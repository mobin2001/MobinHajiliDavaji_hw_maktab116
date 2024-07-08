
class AuthException(BaseException):

    def __str__(self) -> str:
        return super().__str__()
    
class UsernameAlreadyExists(AuthException):
    
    def __str__(self) -> str:
        return "Error Username Already Exists"
    
class PasswordTooShort(AuthException):
    
    def __str__(self) -> str:
        return "Error Password should be al least 8 chars"
    
class InvalidUsername(AuthException):

    def __str__(self) -> str:
        return "Error Invalid user name"

class InvalidPassword(AuthException):

    def __str__(self) -> str:
        return "Error Invalid Password"
        
    