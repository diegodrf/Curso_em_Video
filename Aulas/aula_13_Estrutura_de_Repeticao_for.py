#ver o ajuste de brilho no diolinux

for c in range(0, 6): # Executa 6x
    print('oi')
print('FIM1')

#=========================
for c in range(1, 7): # Executa 6x, pois ele sempre ignora o último número
    print('oi')
print('FIM2')

#=========================
for c in range(0, 7): # Escreve o número de c que corresponde a quantidade de loops
    print(c)
print('FIM3')

#=========================
for c in range(6, 0, -1): # Escreve o número de c contando inversamente, assim como no caso da manipulação de strings
    print(c)
print('FIM4')

#=========================
for c in range(0, 7, 2): # Escreve pulando duas casas, assim como no caso da manipulação de strings
    print(c)
print('FIM5')

#========================
i = int(input('Inicio: ')) # Loop definido pelo usuário
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('FIM6')

#======================
for c in range(1,11):   # Repete os comandos de interação com o usuário
    n = input('Informe o {}ª valor: '.format(c))
print('FIM7')

#=======================
s = 0                       # Pega os números fornecidos pelo usuário e soma em loop.
for c in range(1, 4):
    n = int(input('Informe o {}º número: '.format(n)))
    s += n
print('O somatório dos número é: {}'.format(s))