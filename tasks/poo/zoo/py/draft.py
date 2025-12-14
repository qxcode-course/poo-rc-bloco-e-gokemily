from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome:str):
        self.__nome = nome

    def setNome(self, nome: str):
        self.__nome = nome

    def getNome(self) -> str:
        return self.__nome
    
    def apresentar_nome(self):
        print(f'Eu sou um(a) {self.getNome()}!')

    @abstractmethod
    def fazer_som(self):
        pass
    @abstractmethod
    def mover(self):
        pass

class Leao(Animal):
    def __init__(self, nome:str):
        super().__init__(nome)

    def fazer_som(self):
        print('uraarr')
    
    def mover(self):
        print('correndo')

class Elefante(Animal):
    def __init__(self, nome:str):
        super().__init__(nome)

    def fazer_som(self):
        print('Fuumm uuuuh')
    
    def mover(self):
        print('correndo pesado')

class Cobra(Animal):
    def __init__(self, nome:str):
        super().__init__(nome)

    def fazer_som(self):
        print('siiiiuuu')
    
    def mover(self):
        print('rastejando')

def apresentar(animal: Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    print(type(animal))

animais = [
    Leao('mufasa'),
    Elefante('dumbo'),
    Cobra('Gary, a cobra'),
    Leao('Simba')
]

for i in animais:
    apresentar(i)