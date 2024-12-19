km = int(input('Distntâcia da viagem: '))
print('\nAnálisando distância {}km...\n'.format(km))

if km <= 200:
    print('Sua viagem de {}km e terá o preço de R${:.2f}\n'.format(km, km * 0.5))
else:
    print('Sua viagem de {}km e terá o preço de R${:.2f}\n'.format(km, km * 0.45))