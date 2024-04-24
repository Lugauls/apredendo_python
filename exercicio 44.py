pn = float(input('Digite o preço do produto: '))
print('-='*10)
print('''Digite [1] para á vista com 10'%' de desconto 
Digite [2] para á vista no cartão para 5'%' de desconto
Digite [3] para até 2x no cartão com preço normal
Digite [4] para 3x ou mais vezes no cartão com 20'%' de juros''')
print ('-='*10)
cp = int(input('Qual é sua escolha: '))
if cp > 4:
    print('opção inválida')
elif cp == 1:
    print(f'O pagamento á vista é igual a {pn - (pn*10/100)}.')
elif cp == 2:
    print(f'O pagamento no cartão á vista é {pn - (pn*5/100)}.')
elif cp == 4:
    parc = int(input('Quantas Parcelas:'))
    print(f'A parcela de {parc}x sai ${(pn + (pn*20/100))/parc} por mês')
    print(f'O pagamento em {parc}x é {pn + (pn*20/100)}, com juros.')
else:
    print(f'A parcela é {pn/2}')
    print(f'O pagamento em 2x sai o valor total de {pn}, sem juros')