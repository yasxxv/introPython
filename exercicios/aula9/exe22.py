#desafio 22
nome = str(input('Digite o seu nome completo: '))
print('Tudo em minuscula: {}'.format(nome.lower()))
print('Tudo em maiusco: {}'.format(nome.upper()))
print('Seu nome possui {} letras'.format(len(nome.replace(' ', ''))))
dividido = nome.split()
print('{} tem {} leras'.format(dividido[0],len(dividido[0])))