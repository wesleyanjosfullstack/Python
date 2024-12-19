a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
print('\nAnálisando os seguite valores: {}, {}, {}...\n'.format(a, b, c))

me = a

if  b < a and b < c:
    me = b
if  c < a and c < b:
    me = c

print('O menor valor digitado foi: {}\n'.format(me))

ma = a

if b > a and b > c:
    ma = b
if c > a and c > b:
    ma = c

print('O maior valor digitado foi: {}\n'.format(ma))