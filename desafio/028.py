from random import randint

pc = randint(0, 5)
user = int(input('Digite um número entre 0 e 5: '))

if user == pc:
    print('Parabéns, voçê venceu !\n PC número: {} e Usuário núremo: {}\n'.format(user, user))
else:
    print('Errou !\nPC número: {} e Usuário núremo: {}\n'.format(user, user))