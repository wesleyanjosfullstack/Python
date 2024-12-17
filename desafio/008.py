m = float(input('Digite um valor em metros: '))
print('=' * 30)
print('Médida de {:.1f}m corresponde á:'.format(m))
print('=' * 30)

cm = m * 100
mm = m * 1000
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10

print('Quilometros: {:.3f}km\nHectômetro: {:.2f}hm'.format(km, hm))
print('Decâmetro: {:.1f}dam\nDecímetro: {:.0f}dm'.format(dam, dm))
print('Centimetros: {:.0f}cm\nMilimetros: {:.0f}mm\n'.format(cm, mm))