# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo
# de 1 até 500.
soma = 0
quantidade = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        quantidade += 1
print('A soma é {}.'.format(soma))
print('Total de números: {}'.format(quantidade))