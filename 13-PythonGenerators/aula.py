def fibonacci(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for number in fibonacci(10):
    print(number)

# Uso do yield
# Vantagem que os valores (lista) não ficam salvos na memória


def simple_gen():
    for x in range(3):
        yield x

# Assign simple_gen 
g = simple_gen()

print(next(g))

print(next(g))

print(next(g))

# print(next(g))

# Para tornar uma string em um iterador
word = 'palavra'
novo_iterador = iter(word)
print(next(novo_iterador))
print(next(novo_iterador))
print(next(novo_iterador))