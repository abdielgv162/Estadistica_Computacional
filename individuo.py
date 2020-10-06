import random

class Individuo:
    def __init__ (self,nombre):
        self.nombre = nombre

class Aleatorio_Tradicional(Individuo):
    def __init__ (self, nombre):
        super().__init__(nombre)
    def camina(self):

        return random.choice([(0,1),(0,-1),(1,0),(-1,0)])

class Aleatorio_ArribaAbajo(Individuo):
    def __init__(self,nombre):
        super().__init__(nombre)
    
    def camina(self):
        return random.choice([(0,-3),(0,3),(-1,0),(1,0)])