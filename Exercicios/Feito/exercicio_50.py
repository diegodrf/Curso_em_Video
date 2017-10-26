# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor for ímpar,
# desconsidere-o.
soma = 0
for c in range(1, 7):
    numero = int(input('{}º número: '.format(c)))
    if numero % 2 == 0:
        soma += numero
print('A soma dos números PARES digitados é: {}'.format(soma))