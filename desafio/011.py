width = float(input('Digite a largura da parede: '))
height = float(input('Digite a altura da parede: '))
zone = width * height
t = zone / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}\nPara pintar essa parede, voçê precisa de {}l de tinta.\n'.format(width, height, zone, t))