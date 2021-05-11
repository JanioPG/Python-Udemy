# Herança
'''class Animal():
    def __init__(self):
        print('ANIMAL CREATED')
    

    def who_am_i(self):
        print('I am an animal')
    
    def eat(self):
        print('I am eating')


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def eat(self):
        print('I am a dog and eating')

    def who_am_i(self):
        print('I am a dog')


# Polimorfismo

class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!'

tony = Dog('Tony')
felix = Cat('Felix')

# outra demonstração: po iteração
for pet in [tony, felix]:
    print(type(pet))
    print(type(pet.speak()))
    print(pet.speak())'''

# Outra demonstração: por função
def pet_speak(pet):
    print(pet.speak())

# Classes e herança
class Animal():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("A subclasse deve implementar esse método abstrato")
        # Espera que a subclasse herde e susbtitua o método abstrato

class Dog(Animal):

    def speak(self):
        return self.name + ' says woof!'

    
class Cat(Animal):

    def speak(self):
        return self.name + ' says meow!'


tony = Dog('Tony')
gato = Cat('gato')
print(tony.speak())
print(gato.speak())
