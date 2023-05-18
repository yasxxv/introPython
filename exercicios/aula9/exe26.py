#desafio 26 
frase = str(input('Digite uma frase abaixo: ').upper().strip())
la = frase.count('A')
print(f'Está frase possui:{la} Letras "a"')
f2 = frase.find('A')
f3 = f2 + 1
print(f'Está letra aparece pela primeira vez na: {f3}° posição da frase.')
f4 = frase.rfind('A')
f5 = f4 + 1
print(f'Está letra aparece pela ultima vez na: {f5}° posição da frase.')