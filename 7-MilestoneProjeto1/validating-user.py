import os

def display_game(game_list):
    print('Here is the current list')
    print(game_list)

def clear_output():
    """
    -> Limpa a tela quando é chamada
    """
    os.system('cls' if os.name == 'nt' else 'clear')


#Escolhendo posição
def position_choice():
    choice = 'WRONG'
    while choice not in ['0', '1', '2']:
        choice = input('Pick a position to replace (0, 1, 2): ')
        if choice not in ['0', '1', '2']:
            clear_output()
            print('Sorry, but you did not choose a valid position (0, 1, 2)')
    return int(choice)

def replacement_choice(game_list, position):
    user_placement = input('Type a string to place at the position: ')
    game_list[position] = user_placement
    return game_list

def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y', 'N']:
        choice = input('Would you like to keep playing? Y or N: ')
        if choice not in ['Y', 'N']:
            clear_output()
            print("Sorry, I didn't understand. Please make sure to choose Y or N")
    if choice == 'Y':
        return True
    else:
        return False

# Validating User Input
def user_choice():
    choice = 'WORNG'
    acceptable_range = range(0, 10)
    within_range = False
    while choice.isdigit() == False or within_range == False:
        choice = input('Please enter a number (0-10): ')
        if choice.isdigit() == False:
            print('Sorry that is not a digit.')
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Sorry, you are out of acceptable range (0-10)')
                within_range = False
    return int(choice)
        

# Game logic all together
game_on = True
game_list = [0, 1, 2]

while game_on:

    # Limpar e mostrar o jogo
    clear_output()
    display_game(game_list)

    # Fazer o jogador escolher a posição
    position = position_choice()
    game_list = replacement_choice(game_list, position)

    # Limpar a tela e mostrar o jogo
    clear_output()
    display_game(game_list)

    # Perguntar se o usuário quer continuar o jogo
    game_on = gameon_choice()