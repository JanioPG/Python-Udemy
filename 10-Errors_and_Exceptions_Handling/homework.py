# Problema 1
def problem1():
    try: 
        for i in ['a', 'b', 'c']:
            print(i ** 2)
    except:
        print('Error: Operação não suporta a potência de uma string')

# Problema 2
def problem2():
    try:
        x = 5
        y = 0
        z = x / y
    except ZeroDivisionError:
        print('Error: A divisão por zero é uma indefinição matemática.')
    finally:
        print('All Done')

# Problema 3
def ask():
    while True:
        try:
            number = int(input('Please enter an integer: '))
        except:
            print('Ocorreu um erro. Por favor, tente novamente.')
        else:
            break
    valor = number ** 2
    print(f'Thank you, your number squared is: {valor}')
    
if __name__ == '__main__':
    problem1()
    problem2()
    ask()
