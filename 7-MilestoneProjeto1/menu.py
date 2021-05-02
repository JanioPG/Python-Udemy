import interface
import os
import jogodavelha
import menuMatriz
from functions import limpar_tela

limpar_tela()

msg_erro = ''
while True:
    interface.head('Menu Principal')
    print('''O que deseja:
    [1] Gerar matriz e ver as subdivisões
    [2] Jogar jogo da Velha
    [3] Sair''')
    print(msg_erro)
    action = str(input('Opção: ')).strip()
    limpar_tela()

    if action == '1':
        menuMatriz.gerar_matrizes()
        msg_erro = ''
    elif action == '2':
        jogodavelha.apresentação()
        msg_erro = ''
    elif action == '3':
        break
    else:
        msg_erro = '\033[31mOpção inválida. Escolha um número inteiro válido.\033[m'

print('\033[32mPrograma encerrado\033[m\n')