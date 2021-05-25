# 1) Create a generator that generates the squares of numbers up to some number N.
print('\nExercício 1:')
def quadrado(N):
    for value in range(N):
        yield value ** 2

for x in quadrado(10):
    print(x)

# 2) Create a generator that yields "n" random numbers between
# a low and high number (that are inputs). Note: Use the random library. For example:
print('\nExercício 2:')
from random import randint

def rand_num(inicio, fim, vezes):
    for x in range(vezes):
        yield randint(inicio, fim)

for value in rand_num(1, 10, 5):
    print(value)

# 3) Use the iter() function to convert the string below into an iterator:
print('\nExercício 3:')
word = 'palavra'
nnovo_iterador = iter(word)
print(next(nnovo_iterador))

# 4) Explain a use case for a generator using a yield statement where you
# would not want to use a normal function with a return statement.
'''
Quando eu quiser apenas fazer uma iteração, ou seja,
sem que os valores sejam armazenados na memória.
'''

# 5)
print('\nExercício 5:')
my_list = [1, 2, 3, 4, 5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)