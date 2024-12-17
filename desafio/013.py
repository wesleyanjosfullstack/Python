s = float(input('Digite o valor do salário: R$'))
ns = s + (s * 15 / 100)
print('Salário: R${:.2f}, com um aumento de 15% R${:.2f}'.format(s, ns))