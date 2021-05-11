import os
import keyboard

class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, value):
        self.balance += value
        print(f'Depósito de R${value:.2f} realizado com sucesso.')

    def withdraw(self, value):
        if value < self.balance:
            self.balance -= value
            print('Saque disponível. Aguarde e retire o dinheiro.')
        else:
            print('Desculpe, valor do saque acima do saldo disponível.')

    def __str__(self):
        return f'Proprietário: {self.owner} \nSaldo: R${self.balance:.2f}'.replace('.', ',')


# Programa principal
os.system('cls' if os.name == 'nt' else 'clear')
name = str(input('Nome: '))
saldo = 100
msg_erro = ''
account1 = Account(name, saldo)

while True:
    print('''Banco Python
    O que deseja?
    [1] Dados do proprietário
    [2] Nome registrado
    [3] Saldo disponível
    [4] Depósito
    [5] Saque
    [6] Sair
    ''')
    print(msg_erro)
    action = str(input('Opção: ')).strip()
    if action not in ['1', '2', '3', '4', '5', '6'] or len(action) == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        msg_erro = 'Desculpe, opção inválida. Escolha um número inteiro válido.'
        continue
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        if action == '1':
            print(account1)
        elif action == '2':
            print(account1.owner)
        elif action == '3':
            print(account1.balance)
        elif action == '4':
            deposito = int(input('Valor do depósito: R$'))
            account1.deposit(deposito)
        elif action == '5':
            saque = int(input('Valor do saque: R$'))
            account1.withdraw(saque)
        else:
            break
    print("\nPressione 'esc' para sair")
    keyboard.wait('esc')
    os.system('cls' if os.name == 'nt' else 'clear')
