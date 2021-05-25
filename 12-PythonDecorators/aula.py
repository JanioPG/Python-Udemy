# Criando um Decorador
def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func
'''
def func_needs_decorator():
    print("This function is in need of a Decorator")

Reassign func_needs_decorator
func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()

Um decorador simplesmente encapsulou a função e modificou seu comportamento. Agora vamos entender como podemos reescrever esse código usando o símbolo @, que é o que o Python usa para decoradores:
'''

@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")