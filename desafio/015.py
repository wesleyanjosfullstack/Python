day = int(input('Quantos dias alugados ? '))
km = float(input('Quantos Km rodados ? '))
pay = (day * 60) + (km * 0.15) 
print('O total a pagar é de R${:.2f}'.format(pay))