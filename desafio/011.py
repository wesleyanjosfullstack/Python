width = float(input('Digite a largura da parede: '))
height = float(input('Digite a altura da parede: '))
zone = width * height
t = zone / 2
print('Largura da parede: {:.2f}m\nAltura da parede: {:.2f}m\nÁrea: {:.2f}m²\nTinta : {:.2f}l'.format(width, height, zone, t))