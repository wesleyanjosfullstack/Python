number = int(input('Digite um valor entre 0 a 9999: '))
print('\nAnálisando o número {}...\n'.format(number))

u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('milhar: {}'.format(m))