text = 'Curso em Vídeo Python'
print(text[3])
print(text[3:13])
print(text[:13])
print(text[13:])
print(text[1:15])
print(text[1:15:2])
print(text[1::2])
print(text[::2])
print('oi')
print('-' * 30)
print('''Bem-vindo ! 
Olá a todos ao mundo da programação em Python, 
podemos programar sistemas desktop, web e app.''')
print('-' * 30)
print(text.count('O'))
print(text.count('o'))
print(text.upper().count('O'))
print(text.lower().count('o'))
print(len(text))
text = '   Curso em Vídeo Python  '
print(len(text.strip()))
text = 'Curso em Vídeo Python'
print(text.replace('Python', 'Android'))
print(text[0])

text = text.replace('Python', 'Php')
print(text)

print(text.find('Curso'))
print(text.find('Vídeo'))
print(text.lower().find('vídeo'))
print(text.split())
div = text.split()
print(div[0])
print(div[2][3])