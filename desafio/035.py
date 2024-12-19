print('=' * 30)
print('Análisando de Triângulo')
print('=' * 30)

l1 = float(input('Digite o primeiro comprimento: '))
l2 = float(input('Digite o segundo comprimento: '))
l3 = float(input('Digite o terceiro comprimento: '))

print('\nAnálisando os comprimentos: {}, {} e {}...\n'.format(l1, l2, l3))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Podem forma um triângulo\n')
else:
    print('Não podem forma um triângulo\n')