class Singleton(object):

    def __new__(cls):
        pass



akbar = Singleton()
asgar = Singleton()
        
print(akbar == asgar)
print(akbar is asgar)
print(id(akbar) == id(asgar))

