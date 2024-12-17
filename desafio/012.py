p = float(input('Valor do produto: R$'))
r = p - (p * 5 / 100)
print('Produto R${:.2f}, com desconto de 5%, R${:.2f}'.format(p, r))