'''44 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

    - À vista dinheiro / cheque: 10% de desconto;
    - À vista no cartão: 5% de desconto;
    - Em até 2x no cartão: preço normal;
    - 3x ou mais no cartão: 20% de juros;'''

print('{:=^40}'.format(' LOJAS GUANABARA ')) # ^40 centraliza com 40 caracteres para cada lado, = preenche os espaços com o símbolo =
valor = float(input('Valor: R$ '))
modo=int(input('Qual é a forma de pagamento?\n1- Dinheiro / Cheque\n2- Cartão\n'))

if modo == 1:
    valor = valor - (valor * 10)/100
    print('Total: R$ {:.2f}'.format(valor))
elif modo == 2:
    parcela=int(input('Quantas parcelas?\n1- À vista\n2- 2x\n3- 3x ou mais:\n'))
    if parcela == 1:
        valor = valor - (valor * 5)/100
        print('Total: R$ {:.2f}'.format(valor))
    elif parcela == 2:
        print('Total R$ {:.2f}'.format(valor))
    else:
        valor = valor + (valor * 20)/100
        print('Total R$ {:.2f}'.format(valor))