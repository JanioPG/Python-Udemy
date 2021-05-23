from random import shuffle
from entrada import Entrada

class Carta:

    def __init__(self, naipe, rank, value):
        self.naipe = naipe
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} de {self.naipe}"


class Baralho:

    naipes = ('Copas', 'Ouros', 'Espadas', 'Paus')
    ranks = {'Dois': 2, 'Três': 3, 'Quatro': 4, 'Cinco': 5, 'Seis': 6, 'Sete': 7, 'Oito': 8, 'Nove': 9, 'Dez': 10, 'Valete': 10, 'Rainha': 10, 'Rei': 10, 'Ás': 11}

    def __init__(self):
        self.baralho = []
        for naipe in self.naipes:
            for rank, value in self.ranks.items():
                self.baralho.append(Carta(naipe, rank, value))

    def embaralhar(self):
        """-> Embaralha o baralho
        """
        shuffle(self.baralho)

    def pegar_uma_carta(self):
        """-> Pega uma carta do objeto baralho
        Returns:
            Carta: uma carta do baralho. 
        """
        uma_carta = self.baralho.pop()
        return uma_carta


class Hand:
    
    def __init__(self):
        self.cartas = []
        self.pontos = 0
        self.num_carta_as = 0

    def adicionar_carta(self, carta):
        """-> Adiciona carta na mao do jogador
        Args:
            carta (Carta): uma carta do objeto baralho.
        """
        self.cartas.append(carta)
        self.pontos += carta.value
        if carta.rank == 'Ás':
            self.num_carta_as += 1
    
    def ajustar_pontos(self):
        """-> Faz o ajuste com a carta Ás. Verifica se há Ás na mao do jogador,
        caso verdadeiro e necessário, pode substrair 10 pontos.
        """
        if self.pontos > 21 and self.num_carta_as > 0:
            self.pontos -= 10
            self.num_carta_as -= 1
        

class Fichas:

    def __init__(self):
        self.total = 70

    def ganhou(self, aposta):
        self.total += aposta
    
    def perdeu(self, aposta):
        self.total -= aposta
    
    def __str__(self):
        return f"Total de fichas: {self.total}"


class User:

    def __init__(self):
        self.name = 'Jogador'
        self.saldo = 50
        self.ficha = Fichas()
        self.hand = Hand()

    def identificar(self):
        identificar = Entrada('\nGostaria de se identificar [y/n]? ', 'y', 'n', 'Y', 'N').caractere()
        if identificar in ('y', 'Y'):
            self.name = Entrada('Nome: ').caractere()

class Operation:

    def __init__(self):
        pass

    def jogador_ganhou(self, pontos_dealer, pontos_jogador):
        if pontos_dealer > pontos_jogador:
            return False
        elif pontos_dealer < pontos_jogador:
            return True
    
    def verificar_empate(self, pontos_dealer, pontos_jogador):
        if pontos_dealer == pontos_jogador:
            return True
        return False

    def jogar_novamente(self):
        continuar = Entrada('Gostaria de jogar novamente[y/n]? \nEscolha: ', 'y', 'Y', 'n', 'N').caractere()
        if continuar in ('y', 'Y'):
            return True
        return False

    def solicitar_aposta(self, total_fichas):
        while True:
            aposta = Entrada('Quantas fichas gostaria de apostar: ').num_inteiro()
            if aposta <= total_fichas:
                return aposta
            else:
                print(f'Aposta acima do número de fichas disponíveis. Suas fichas: {total_fichas}')
                continue



        