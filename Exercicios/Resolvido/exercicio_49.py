# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
a = int(input('Informe o número da tabuada desejada: '))
for c in range(0, 11):
    print('{} x {} = {}'.format(a, c, a*c))