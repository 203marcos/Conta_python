class Cliente:
    
    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self): 
        print("Chamando a funçao")
        return self.__nome.title()    
    