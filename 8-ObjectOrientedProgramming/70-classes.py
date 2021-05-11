class Dog():
    # Class object attribute
    espécie = 'mamífero'

    # Método construtor
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots
    

    # Operações/ações --> Methods
    def bark(self, number):
        print(f'Woof! My name is {self.name} e o número é {number}')


class Circle():
    from math import pi
    valor_pi = pi

    def __init__(self, radius):
        self.radius = radius
        self.area = radius * radius * Circle.pi
    
    def get_circumference(self):
        return 2 * Circle.pi * self.radius

circulo = Circle(30)
print(circulo.pi)