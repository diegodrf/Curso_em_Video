# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

peso = float(input('1º peso: '))
pesado = peso
leve = peso
for c in range(2, 6):
    peso = float(input('{}º peso: '.format(c)))
    if peso >= pesado :
        pesado = peso
    elif peso <= leve:
        leve = peso
print('Mais pesado: {} Kg\nMais leve: {} Kg'.format(pesado, leve))