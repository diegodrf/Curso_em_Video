# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

numero_user = 11
numero_cpu = randint(0,10)
contador = 0
print('O PC pensou em um número entre 0 e 10. Tente adivinhar!')

while numero_user != numero_cpu:
    numero_user = int(input('Número: '))

    if numero_user != numero_cpu:
        if numero_user > numero_cpu:
            print('Errou! Menos...')
        elif numero_user < numero_cpu:
            print('Errou! Mais...')

    contador += 1

print('\n\nVocê acertou!!!\n\nO número pensado foi {}.\n\nVocê precisou de {} tentativas!'.format(numero_cpu,contador))
