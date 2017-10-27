# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
n = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
for c in range(0, r*10, r):
    print(n)
    n += r