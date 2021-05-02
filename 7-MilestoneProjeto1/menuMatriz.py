import interface
from functions import limpar_tela, esperar_usuario
from random import randint


def nova_matriz():
    matriz = [[], [], [], []]
    for l in range(0, 4):
        for c in range(0, 4):
            number = randint(1, 20)
            #number = int(input(f'Valor para a posição [{l + 1}x{c + 1}]: '))
            matriz[l].append(number)
    return matriz


def gerar_matrizes():
    matriz = nova_matriz()
    msg_erro = ''
    while True:
        interface.head('Menu Principal')
        print('''O que deseja ver?
        [1] Matriz completa
        [2] Diagonal principal
        [3] Triângulo superior
        [4] Triângulo inferior
        [5] Sair''')
        print(msg_erro)
        action = str(input('Opção: ')).strip()
        limpar_tela()

        if action == '1':
            interface.matriz_completa(matriz)
        elif action == '2':
            interface.diagonal_principal(matriz)
        elif action == '3':
            interface.triangulo_superior(matriz)
        elif action == '4':
            interface.triangulo_inferior(matriz)
        elif action == '5':
            break
        else:
            msg_erro = '\033[31mOpção inválida. Escolha um número inteiro válido.\033[m'
            continue
        msg_erro = ''
        esperar_usuario()