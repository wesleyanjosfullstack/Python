l1 = int(input('Digite o primeiro comprimento: '))
l2 = int(input('Digite o segundo comprimento: '))
l3 = int(input('Digite o terceiro comprimento: '))
print('\nAnálisando os comprimentos: {}, {} e {}...\n'.format(l1, l2, l3))

if l1 == l2 and l1 == l3:
    print('Podem forma um triângulo equilatero\n')
else:
    if l1 != l2 and l1 != l3 and l2 != l3:
        print('Não pode forma um triângulo !\n')