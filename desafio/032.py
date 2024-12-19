from datetime import date

y = int(input('Digite qualquer ano ou digite 0 para o ano atual: '))

if y == 0:
    y = date.today().year

print('\nAnálisado o ano {}...\n'.format(y))

if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print('Ano bissexto !\n')
else: 
    print('Ano não bissexto !\n')