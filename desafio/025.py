name = str(input('Digite seu nome: ')).strip().upper()
print('\nAnálisando o nome {}...\n'.format(name))
print('Seu nome tem Silva ? {}'.format('SILVA' in name))