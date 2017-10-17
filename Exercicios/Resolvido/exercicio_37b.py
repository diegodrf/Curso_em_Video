'''37 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

    -1 para binário;
    -2 para octal;
    -3 para hexadecimal;'''

num=int(input('Informe um número inteiro: '))
escolha = 0
while (escolha > 3) or (escolha < 1):
    escolha=int(input('1- Binário\n2- Octal\n3- Hexadecimal\nEscolha: '))
    if escolha == 1:
        # conversão para binário
        print(bin(num)[2:])

    elif escolha == 2:
        # conversão para octal
        print(oct(num)[2:])

    elif escolha == 3:
        # conversão para hexadecimal
        print(hex(num).upper()[2:])
