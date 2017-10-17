nome = str(input('Qual é seu nome? ')).lower()
if nome == 'gustavo':
    print('Que nome bonito!')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem normal')

print('Tenha um bom dia, {}!'.format(nome))