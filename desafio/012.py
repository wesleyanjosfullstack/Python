p = float(input('Valor do produto: R$'))
d = p * (5 / 100)
r = p - d
print('Produto R${:.2f}, com desconto de 5%, R${:.2f}'.format(p, r))