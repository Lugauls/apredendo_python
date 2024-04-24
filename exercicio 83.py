pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Digite um nome:')))
    dados.append(float(input('Digite um peso:')))
    if len(pessoas) == 0 :
       maior = menor = dados[1]
    else:
        if dados [1]> maior:
            maior = dados[1]
        else:
            menor = dados [1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Você quer continuar[S/N]:')).upper()
    if continuar == 'N' or continuar != 'S':
        break
print(f'O número de pessoas cadastradas são {len(pessoas)}')
print(f'O maior peso foi de {maior}kg',end=' ')
for x in pessoas:
     if x[1] == maior:
        print(f'[{x[0]}]',)
print(f'O menor peso foi de {menor}kg',end=' ')
for c in pessoas :
    if c[1] == menor:
        print(f'[{c[0]}]',)