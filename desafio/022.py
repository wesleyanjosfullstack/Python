name = str(input('Digite seu nome completo: '))
print('Seu nome é {}'.format(name))
print('Seu nome em maiúsculas {}'.format(name.upper()))
print('Seu nome em minúsculas {}'.format(name.lower()))
first = name.split()
print('Quantidades de letras sem espaços: {}'.format(len(name[::1])))
print('Quantidades de letras no primeiro nome: {} letras'.format(len(first[0])))