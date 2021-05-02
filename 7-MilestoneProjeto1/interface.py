# Funções para exibir ao usuário

def head(text):
    print('\033[36m-=\033[m' * 15)
    print(text.center(30))
    print('\033[36m-=\033[m' * 15)


# Matriz
def matriz_completa(lista):
    matriz = lista
    head('Matriz 4x4')
    for line in matriz:
        for column in line:
            print(f'{column:^4} ', end='')
        print()
    print()

# Diagonal Princial
def diagonal_principal(lista):
    matriz = lista
    head('Diagonal Principal')
    for i, line in enumerate(matriz):
        for c, column in enumerate(line):
            if i == c:
                print(f'\033[33m{column:^4}', end='')
            else:
                print(f'{" ":^4}', end='')
        print()
    print('\033[m')


# Triângulo superior
def triangulo_superior(lista):
    matriz = lista
    head('Triângulo superior')
    for i, line in enumerate(matriz):
        for c, column in enumerate(line):
            if i < c:
                print(f'\033[32m{column:^4}', end='')
            else:
                print(f'{" ":^4}', end='')
        print()
    print('\033[m')

# Triângulo inferior
def triangulo_inferior(lista):
    matriz = lista
    head('Triângulo inferior')
    for i, line in enumerate(matriz):
        for c, column in enumerate(line):
            if i > c:
                print(f'\033[34m{column:^4}', end='')
            else:
                print(f'{" ":^4}', end='')
        print()
    print('\033[m')