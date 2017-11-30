# Faça um programa que leia um número qualquer e mostre o seu fatorial:
# Ex.: 5! = 5x4x3x2x1=120
import time
num = int(input('Informe o número fatorial: '))

fatorial = 1

print('{}!'.format(num), end=' = ')
while num > 0:
    if num != 1:
        print('{}'.format(num), end=' x ')
    else:
        print('{}'.format(num), end=' = ')
    fatorial = fatorial * num
    num -= 1
print(fatorial)
