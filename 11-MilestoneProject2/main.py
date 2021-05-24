from interface import Mensagens, ExibirCartas, limpar_terminal
from entrada import Entrada
from objetos_jogo import User, Baralho, Hand, Operation


new_game = True
mensagem = Mensagens()
mesmo_jogador = False

limpar_terminal()

while new_game:
    if not mesmo_jogador:
        # Boas-vindas
        mensagem.boas_vindas()
        jogador = User()
        jogador.identificar()
        limpar_terminal()
        print(f"Bem-vindo, {jogador.name}!")
        print(f'Você ganhou {jogador.ficha.total} fichas para jogar.')
    else:
        # Para novo jogo: Limpar cartas, pontos e numero de carta Ás da mao do jogador. 
        jogador.hand.cartas.clear()
        jogador.hand.pontos = 0
        jogador.hand.num_carta_as = 0

    # Solicitar aposta do jogador
    operacao = Operation()
    aposta_jogador = operacao.solicitar_aposta(jogador.ficha.total)
    limpar_terminal()

    # criar baralho e embaralhar
    baralho = Baralho()
    baralho.embaralhar()

    # Distribuir duas cartas para cada jogador
    mao_dealer = Hand()

    for x in range(4):
        if x < 2:
            carta = baralho.pegar_uma_carta()
            jogador.hand.adicionar_carta(carta)
        else:
            carta = baralho.pegar_uma_carta()
            mao_dealer.adicionar_carta(carta)

    # Exibir cartas
    ExibirCartas().nao_tudo(mao_dealer.cartas, jogador.hand.cartas)

    # perguntar se o jogador deseja mais uma carta

    perdeu = False
    while not perdeu:
        jogador.hand.ajustar_pontos()
        if jogador.hand.pontos > 21:
            limpar_terminal()
            perdeu = True
        else:
            add = Entrada('\nO que deseja?\n[1] Esperar o dealer \n[2] Quero mais uma carta. \nEscolha: ', 1, 2).num_inteiro()
            limpar_terminal()

            if add == 2:
                carta = baralho.pegar_uma_carta()
                jogador.hand.adicionar_carta(carta)
                ExibirCartas().nao_tudo(mao_dealer.cartas, jogador.hand.cartas)
                continue
            else:
                print()
                break
   
    if perdeu:
        jogador.ficha.perdeu(aposta_jogador)
        ExibirCartas().exibir_tudo(mao_dealer.cartas, jogador.hand.cartas)
        mensagem.msg_perdeu(jogador.name)

    else:
        # ajustar mao do dealer. Dealer deve ter no mínimo 17 pontos
        mao_dealer.ajustar_pontos()   # esse ajuste vale se inicialmente tiver 'dois Ás' = 22
        while mao_dealer.pontos < 17:
            carta = baralho.pegar_uma_carta()
            mao_dealer.adicionar_carta(carta)
            mao_dealer.ajustar_pontos()

        # Verificar mao do dealer
        if mao_dealer.pontos > 21:
            ExibirCartas().exibir_tudo(mao_dealer.cartas, jogador.hand.cartas)
            jogador.ficha.ganhou(aposta_jogador)
            mensagem.msg_ganhou(jogador.name)
        else:
            # comparar         
            # empate
            ExibirCartas().exibir_tudo(mao_dealer.cartas, jogador.hand.cartas)
            if operacao.verificar_empate(mao_dealer.pontos, jogador.hand.pontos):
                mensagem.msg_empate()

            # vencedor
            elif operacao.jogador_ganhou(mao_dealer.pontos, jogador.hand.pontos):
                jogador.ficha.ganhou(aposta_jogador)
                mensagem.msg_ganhou(jogador.name)
            else:
                jogador.ficha.perdeu(aposta_jogador)
                mensagem.msg_perdeu(jogador.name)
                
    print(f"\nPontos do dealer: {mao_dealer.pontos} \nPontos do {jogador.name}: {jogador.hand.pontos}\n")

    if jogador.ficha.total == 0:
        new_game = False
        mensagem.game_over()

    else:
        new_game = operacao.jogar_novamente()
        limpar_terminal()
        if new_game:
            mesmo_jogador = True
print(f"Fichas atuais do {jogador.name}: {jogador.ficha.total}")
print('\n\033[32mObrigado por ter jogado. Até a próxima!\n\033[m')
