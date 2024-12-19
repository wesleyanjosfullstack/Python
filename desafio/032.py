year = int(input('Digite qualquer ano: '))
print('\nAnálisado o ano {}...\n'.format(year))

if year % 4 != 0:
    print('Ano não bissexto !\n')
else: 
    print('Ano bissexto !\n')