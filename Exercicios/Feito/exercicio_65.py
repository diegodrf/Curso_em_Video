# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

trigger = False
trigger_start = False
num = 1
contador = 0
total = 0

while trigger == False:
    num = int(input('Informe um número: '))

    total += num
    contador += 1

    if trigger_start == False: #Este campo armazena as primeiras variaveis maior e menor, para que elas possam ser comparadas futuramente. Ele só é executado na primeira rotina do código.
        for c in range(0, 1):
            maior = num
            menor = num
            trigger_start = True

    if maior < num:
        maior = num

    if menor > num:
        menor = num

    opcao = str(input('Deseja continuar? (S) ou (N): ')).upper()
    if opcao == 'S':
        pass
    else:
        trigger = True

print('A média dos números digitados é {}'.format(total / contador))
print('O maior número digitado é: {}'.format(maior))
print('O menos número digitado é: {}'.format(menor))
