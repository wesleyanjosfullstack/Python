sal = float(input('Qual é o valor do salário do funciónario ? '))
print('\nAnálisando o salário R${:.2f}...\n'.format(sal))

if sal <= 1250:
    print('O salário vai ter aumento de 15%, portanto o valor será de R${:.2f}\n'.format(sal + (sal * 15 / 100) ))
else:
    print('O salário vai ter aumento de 10%, portanto o valor será de R${:.2f}\n'.format(sal + (sal * 10 / 100) ))