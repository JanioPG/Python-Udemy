from os import system, name
from random import randint
import keyboard
import functions as ft

def limpar_tela():
    system('cls' if name == 'nt' else 'clear')

def linha():
    print('-' * 22)


# Exibir tabuleiro do jogo
def exibir_board(board, limpar=True):
    if limpar == True:
        limpar_tela()
    else:
        pass
    for i, value in enumerate(board):
        print(f'{value:^7}', end='')
        if i in [2, 5]:
            print()
            linha()
        else:
            if i < 8:
                print('|', end='')
    print()

# Escolha do marcado 'X' or 'O'
def escolher_marcador(jogador1=''):
    if len(jogador1) == 0:
        nome = 'Jogador 1'
    else:
        nome = jogador1
    while True:
        marcador = str(input(f"{nome}: Você quer ser 'X' ou 'O'? ")).upper()
        if marcador not in ['X', 'O']:
            limpar_tela()
            print(f"Desculpe, você precisa escolher digitando 'X' ou 'O'")
            continue
        else:
            if marcador == 'X':
                return ('X', 'O')
            else:
                return ('O', 'X')
            break

# Marcar o board
def marcar_board(board, marcador, posicao):
    board[posicao] = marcador


# verificar se o jogador ganhou
def verificar_ganhador(board, marcador):
    # linhas
    for c in range(0, 7, 3):
        if board[c] == marcador and board[c] == board[c + 1] and board[c] == board[c + 2]:
            return True
    # colunas
    for c in range(0, 3):
        if board[c] == marcador and board[c] == board[c + 3] and board[c] == board[c + 6]:
            return True
    # transversal
    if marcador == board[4]:
        if (board[4] == board[0] and board[4] == board[8]) or (board[4] == board[2] and board[4] == board[6]):
            return True
    return False

# Escolher o primeiro a jogar
def joga_primeiro(jogador1='', jogador2=''):
    if randint(0, 1) == 0:
        if len(jogador1) == 0:
            return 'Jogador 1'
        else:
            return jogador1
    else:
        if len(jogador2) == 0:
            return 'Jogador 2'
        else:
            return jogador2


# Verificar se o lugar escolhido está disponível
def verificar_lugar(board, posicao):
    return board[posicao] == ' '

# Verificar se o board está cheio
def board_cheio(board):
    for c in range(0, 9):
        if verificar_lugar(board, c):
            return False
    return True

def escolher_jogada(board):
    erro = ''
    while True:
        ft.exibir_board(board)
        print(erro)
        posicao = str(input('Escolha a posição da sua jogada (0 a 8): '))
        if len(str(posicao.strip())) == 0:
            erro = '\033[31mOpção inválida. Escolha os lugares disponíveis de 0 a 8\033[m'
            ft.limpar_tela()
            continue
        if posicao.isdigit():
            if int(posicao) not in [0, 1, 2, 3, 4, 5, 6, 7, 8] or not verificar_lugar(board, int(posicao)):
                erro = '\033[31mOpção inválida. Escolha os lugares disponíveis de 0 a 8\033[m'
                ft.limpar_tela()
                continue
            else:
                erro = ''
                return int(posicao)

def jogador_pronto():
    while True:
        pronto = str(input('Você está pronto? [y/n]: ')).lower().strip()
        if pronto not in ['y', 'n'] or len(pronto) == 0:
            limpar_tela()
            print("Desculpe, você precisa digitar 'y' (yes) ou 'n' (no)")
            continue
        if pronto == 'y':
            return True
        else:
            return False


def jogar_novamente():
    while True:
        opcao = str(input('\nGostaria de jogar novamente? [y/n]: ')).lower().strip()
        if opcao not in ['y', 'n'] or len(opcao) == 0:
            limpar_tela()
            print("Desculpe, você precisa digitar 'y' (yes) ou 'n' (no)")
            continue
        if opcao == 'y':
            return True
        else:
            return False

def esperar_usuario():
    print("Pressione \033[32m'esc'\033[m para continuar")
    keyboard.wait('esc')
    limpar_tela()


def instrução_jogo():
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print('\nInstrução: Escolha sua jogada de acordo com a numeração abaixo.\n')
    exibir_board(lista, limpar=False)
    print()
    esperar_usuario()

def nome_usuarios():
    while True:
        identificar = str(input('Gostariam de identificar seus nomes? [y/n]: ')).strip()
        if identificar not in ['y', 'n'] or len(identificar) == 0:
            limpar_tela()
            print("Desculpe, você precisa digitar 'y' (yes) ou 'n' (no)")
            continue
        if identificar == 'n':
            return 'Jogador 1', 'Jogador 2'
        else:
            jogador1 = str(input('Nome do jogador 1: ')).strip()
            jogador2 = str(input('Nome do jogador 2: ')).strip()
            if len(jogador1) == 0:
                jogador1 = 'Jogador 1'
            if len(jogador2) == 0:
                jogador2 = 'Jogador 2'
            return jogador1, jogador2