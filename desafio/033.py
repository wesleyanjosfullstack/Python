n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print('\nAnálisando os seguite valores: {}, {}, {}...\n'.format(n1, n2, n3))

if n1 > n2 and n1 > n3:
    print('O maior é {}\n'.format(n1))
else: 
    if n2 > n1 and n2 > n3:
        print('O maior é {}\n'.format(n2))
    else:
        print('O maior é {}'.format(n3))