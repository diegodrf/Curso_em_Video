'''42 - Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

    - Equilátero: Todos os lados iguais;
    - Isósceles: dois lados iguais;
    - Escaleno: todos os lados diferentes;'''
from exercicio_35 import Triangulo

if Triangulo.possivel == True:
    if (Triangulo.a == Triangulo.b) and (Triangulo.a == Triangulo.c):
        print('Triangulo Equilátero')
    elif (Triangulo.a == Triangulo.b) or (Triangulo.b == Triangulo.c) or (Triangulo.a == Triangulo.c):
        print('Triangulo Isósceles')
    else:
        print('Triangulo Escaleno')
