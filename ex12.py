#desafio 12
valor = float(input('Digite o valor do produto: '))
desconto = valor * 0.05
print('Você ganhou 5% de desconto, então vai ficar: R$ {:.2f}'.format(valor-desconto))