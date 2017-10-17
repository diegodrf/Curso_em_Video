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
        binario=''
        while num >0:

            resto = num % 2
            num = num // 2

            binario = str(resto) + binario

        print(binario)

    elif escolha == 2:
        # conversão para octal
        octal=''
        while num > 0:
            resto = num % 8
            num = num // 8

            octal = str(resto) + octal

        print(octal)

    elif escolha == 3:
        # conversão para hexadecimal
        hexa=''
        while num > 0:
            resto = num % 16
            num = num // 16

            if resto == 10:
                resto = 'A'
            if resto == 11:
                resto = 'B'
            if resto == 12:
                resto = 'C'
            if resto == 13:
                resto = 'D'
            if resto == 14:
                resto = 'E'
            if resto == 15:
                resto = 'F'

            hexa = str(resto) + hexa

        print(hexa)
