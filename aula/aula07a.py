print(5 + 3 * 2)
print(5 ** 2)
print(5 ** 3)
print(19 // 2)
print(19 / 2)
print(18 % 2)
print(122 % 3)
print(4 ** 3)
print(pow(4, 3))
print(81 ** (1 / 2))
print(25 ** (1 / 2))
print(127 ** (1 / 3))
print('=' * 20)

name = input('Qual ´seu nome ? ')
print('Prazer em te conhecer {:20}!'.format(name))
print('Prazer em te conhecer {:>20}!'.format(name))
print('Prazer em te conhecer {:<20}!'.format(name))
print('Prazer em te conhecer {:^20}!'.format(name))
print('Prazer em te conhecer {:=^20}!'.format(name))

n1 = int(input('Um valor: '))
n2 = int(input('Um outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))