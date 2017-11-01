# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

divisores = 0
num = int(input('Informe um número: '))
for c in range(1,num+1):
    if (num % c) == 0:
        divisores += 1
        print('{} é divisível por {}.'.format(num, c))

if divisores > 2:
    print('\nPortanto, {} NÃO é um número primo!'.format(num))
else:
    print('\nPortanto, {} É um número primo!'.format(num))