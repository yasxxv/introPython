#desafio 23 
n = int(input('Digite um numero: '))
u = n // 1 % 10
d = n // 10 % 10 
c = n // 100 % 10 
d = n // 1000 % 10 
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Cetena: {}'.format(c))
print('Milhar: {}'.format(c))