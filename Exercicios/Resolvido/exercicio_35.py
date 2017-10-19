'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

class Triangulo:
    a = float(input('Primeiro segmento: '))
    b = float(input('Segundo segmento: '))
    c = float(input('Terceiro segmento: '))
    possivel = (a < (b + c)) and (b < (a + c)) and (c < (a + b))
    if possivel == True:
        print('É possível criar um triângulo ', end='')
    else:
        print('Não é possível criar um triângulo')