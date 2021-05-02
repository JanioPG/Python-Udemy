import functions as ft
from time import sleep
import interface


def apresentação():
    """
    -> Apresenta o jogo aos usuários e recebe seus nomes
    """
    interface.head('Bem-vindo ao jogo da Velha')
    ft.instrução_jogo()
    nomes = ft.nome_usuarios()
    ft.limpar_tela()
    jogo(nomes[0], nomes[1])


def jogo(nome1:str, nome2:str):
    """
    -> Jogo funcionando

    Args:
        nome1 (str): Nome do jogador 1
        nome2 (str): Nome do jogador 2
    """
    while True:
        board = [' '] * 9
        nome1_marca, nome2_marca = ft.escolher_marcador(nome1)
        vez = ft.joga_primeiro(nome1, nome2)
        ft.limpar_tela()
        print(f"Marcadores:\n{nome1} = '{nome1_marca}' e {nome2} = '{nome2_marca}'")
        print(f'\n{vez}, você começa.')
        pronto = ft.jogador_pronto()

        if pronto:
            jogo_ativo = True
        else:
            jogo_ativo = False
            ft.limpar_tela()

        while jogo_ativo:
            if vez == nome1:
                posicao = ft.escolher_jogada(board)
                ft.marcar_board(board, nome1_marca, posicao)
                if ft.verificar_ganhador(board, nome1_marca):
                    ft.exibir_board(board)
                    print(f'\n\033[34mParabéns, {nome1.upper()}! Você ganhou!\033[m')
                    jogo_ativo = False
                else:
                    if ft.board_cheio(board):
                        ft.exibir_board(board)
                        print('Jogo empatado')
                        break
                    else:
                        vez = nome2
            else:
                posicao = ft.escolher_jogada(board)
                ft.marcar_board(board, nome2_marca, posicao)
                if ft.verificar_ganhador(board, nome2_marca):
                    ft.exibir_board(board)
                    print(f'\n\033[34mParabéns, {nome2.upper()}! Você ganhou!\033[m')
                    jogo_ativo = False
                else:
                    if ft.board_cheio(board):
                        ft.exibir_board(board)
                        print('Jogo empatado')
                        break
                    else:
                        vez = nome1

        if not ft.jogar_novamente():
            ft.limpar_tela()
            break
        ft.limpar_tela()