# Logical Operators: and, or, not
print('Operador and:')
print(1<2 and 7>5)  # True: Ambas as condicoes devem ser satisfeitas
print(1>2 and 7>5)

print('\nOperador or:')
print(1<2 or 7<5)  # True: pelo menos uma das condicoes deve ser satisfeita
print(1>2 or 7<5)

print('\nOperador not:')
# Not retorna o resultado (True or False) oposto da comparacao feita
print(not(1<2 or 7<5))
print(not(1>2 or 7<5))