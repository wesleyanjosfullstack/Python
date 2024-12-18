from math import sin, cos, tan, radians

an = int(input('Digite um ângulo: '))
se = sin(radians(an))
co = cos(radians(an))
ta = tan(radians(an))
print('Seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(se, co, ta))