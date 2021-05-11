# Tratamento de erros e exceções
try:
    file = open('test_file.txt', 'r')
    file.write('Escrevendo algo no arquivo')
except:
    # Posso especificar o tipo de erro ou deixar assim de forma genérica
    # This will only check for an IOError exception and then execute this print statement
    print('Error: Could not find file or read data')
else:
    print('Content written successfully')
    file.close()


# O bloco de código finally: sempre será executado, independentemente de haver uma exceção ou não no bloco de código try
# The finally:

'''def askint():
    while True:
        try:
            val = int(input('Please enter an integer: '))
        except:
            print('Parece que você não inseriu um número inteiro.')
            continue
        else:
            print('Sim, isso é um número inteiro.')
            break
        finally:
            print('Finally, I executed.')
        print(val)'''


# 'Finally, I executed' ou o bloco finally é executado mesmo qunado há exceção e em seguida continue e também quando é executado else e break. Isso ocorre porque com uma cláusula try / except / finally, quaisquer instruções continue ou break são reservadas até depois que a cláusula try for concluída. A cláusula try é finalizada em finally, como 'print(val)' está fora da cláusula try, a instrução break impede sua exceução.

# Ajuste
def askint():
    while True:
        try:
            val = int(input('Please enter an integer: '))
        except:
            print('Parece que você não inseriu um número inteiro.')
            continue
        else:
            print('Sim, isso é um número inteiro.')
            print(val)
            break
        finally:
            print('Finally, I executed.')

askint()