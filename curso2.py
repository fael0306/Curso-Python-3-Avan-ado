from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):
    @abstractmethod
    def som(self):
        pass

class Cachorro(Animal):
    def som(self):
        print("Au au au")
        
class Gato(Animal):
    def som(self):
        print("Meaw meaw meaw")

class Fabrica(object):
    def produzirsom(self, object_type):
        return object_type().som()

if __name__ == "__main__":
    f = Fabrica()
    f.produzirsom(Cachorro)
    f.produzirsom(Gato)
