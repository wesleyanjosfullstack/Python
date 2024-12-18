name = str(input('Digite seu nome: '))

print('Seu nome é {}'.format(name))

s = name.split()

print('Tem Silva ? {}'.format(s[:].upper().find('silva')))