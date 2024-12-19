speed = int(input('Qual a velocidade do automavél: '))
print('\nA velocidade foi de {}km/h...\n'.format(speed))

if speed > 80:
    m = (speed - 80) * 7
    print('Voçê foi multada !\nSerá multado em R$7.00 por cada km acima do limite !\nMulta no valor R${:.2f}\n'.format(m))
else:
    print('Muito bem !\nDirija com seguraça !')