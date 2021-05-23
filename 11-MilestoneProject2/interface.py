from os import name, system


class ExibirCartas:
    def __init__(self):
        pass

    def exibir_tudo(self, cartas_dealer, cartas_jogador):
        print(f"\033[34m{'Cartas do Dealer':^17}\033[m")
        for item in cartas_dealer:
            print(item)
        print(f"\n\033[34m{'Cartas do Jogador':^17}\033[m")
        for item in cartas_jogador:
            print(item)

    def nao_tudo(self, cartas_dealer, cartas_jogador):
        print(f"\033[34m{'Cartas do Dealer':^17}\033[m")
        print(f"\033[3;33m{'Carta para baixo':^17} \033[m")
        print(cartas_dealer[1])
        print(f"\n\033[34m{'Cartas do Jogador':^17}\033[m")
        for item in cartas_jogador:
            print(item)


class Mensagens:

    def __init__(self):
        pass
    
    def linhas(self):
        print('=' * 70)

    def boas_vindas(self):
        print('\033[1;32mBem-vindo ao Jogo BlackJack!\033[m'.center(70))
        print('Meta: chegar o mais perto possível de 21 sem ultrapassar!'.center(70))
        print('O dealer bate até atingir 17. Ases contam como 1 ou 11.'.center(70))
        self.linhas()

    def msg_ganhou(self, quem):
        print(f"\n\033[32m {quem} ganhou!\n\033[m")

    def msg_perdeu(self, quem):
        print(f"\n\033[31m {quem} perdeu.\n\033[m")

    def msg_empate(self):
        print(f"\n\033[33m Empate!\n\033[m")
    
    def game_over(self):
        print('Fichas esgotadas.')
        print('\033[31m\n Game Over \n\033[m')


def limpar_terminal():
    system('cls' if name == 'nt' else 'clear')
    Mensagens().linhas()