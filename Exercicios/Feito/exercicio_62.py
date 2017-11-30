# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele
# disser que quer mostrar 0 termos.
from time import sleep
from os import system
ciclos = 0
trigger_start = False
texto = ''
while True == True:

    if trigger_start == False:
        termo = int(input('Informe o primeiro termo da PA: '))
        razao = int(input('Informe a razão da PA: '))
        quant_termos = int(input('Informe a quantidade de termos que deseja ver: '))
        trigger_start = True

    sleep(0.5)
    system('clear')
    texto = texto + str(termo) + ' > '
    print(texto)



    termo += razao

    ciclos += 1

    if ciclos == quant_termos:
        quant_termos = int(input('\nCaso deseje visualizar mais termos, informe a quantidade (Digite 0 para parar): '))

        if quant_termos == 0:
            exit(0)
        else:
          ciclos = 0


