from random import shuffle

suits = ('Copas', 'Ouros', 'Espadas', 'Paus')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card:
    
    def __init__(self, naipe, posicao):
        self.naipe = naipe
        self.posicao = posicao
        self.value = values[posicao]

    def __str__(self):
        return self.posicao + ' of ' + self.naipe


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))
    
    def shuffle(self):
        shuffle(self.all_cards)

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        # a new player has no cards
        self.all_cards = []

    def remove_one(self):
        # remover o topo do baralho com o índice 0, [-1] é a parte de baixo.
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

# Programa Principal
# Game setup

player_1 = Player('Tony Bento')
player_2 = Player('Nina Maria')

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_1.add_cards(new_deck.deal_one())
    player_2.add_cards(new_deck.deal_one())


game_on = True
round_num = 0

while game_on:

    round_num += 1
    print(f'Round {round_num}')

    # Verificar se um jogador está sem cartas
    if len(player_1.all_cards) == 0:
        print('Player One out of cards! Game over')
        print('Player Two wins!')
        game_on = False
        break

    if len(player_2.all_cards) == 0:
        print('Player Two out of cards! Game over')
        print('Player One wins!')
        game_on = False
        break

    # Caso contrário, o jogo continua
    # Comece uma nova rodada e reinicie as cartas atuais "na mesa"
    player_1_cards = []
    player_1_cards.append(player_1.remove_one())

    player_2_cards = []
    player_2_cards.append(player_2.remove_one())

    at_war = True

    while at_war:

        if player_1_cards[-1].value > player_2_cards[-1].value:
            # O jogador 1 recebe as cartas
            player_1.add_cards(player_1_cards)
            player_1.add_cards(player_2_cards)

            # Não está mais na guerra, é hora da próxima rodada
            at_war = False

        elif player_1_cards[-1].value < player_2_cards[-1].value:
            # O jogador 2 recebe as cartas
            player_2.add_cards(player_1_cards)
            player_2.add_cards(player_2_cards)

            # Não está mais na guerra, é hora da próxima rodada
            at_war = False
        
        else:
            print('WAR!')
            # Isso ocorre quando as cartas são iguais.
            # Pegaremos outra carta cada e continuaremos a guerra atual.

            # Primeiro verifique se o jogador tem cartas suficientes
            
            # Verifique se um jogador está sem cartas:
            if len(player_1.all_cards) < 7:
                print('Player 1 unable to play war. Game over at war')
                print('Player 2 Wins. Player 1 Loses.')
                game_on = False
                break

            elif len(player_2.all_cards) < 7:
                print('Player 2 unable to play war. Game over at war')
                print('Player 1 Wins. Player 1 Loses.')
                game_on = False
                break

            # Caso contrário, ainda estamos em guerra, então adicionaremos as próximas cartas
            else:
                for x in range(7):
                    player_1_cards.append(player_1.remove_one())
                    player_2_cards.append(player_2.remove_one())
