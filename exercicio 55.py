#lista = []
#for x in range(1,6):
#    peso = float(input(f'{[x]}Digite seu peso: '))
#    lista += [peso]
#print(f'O maior peso foi {max(lista)} e o menor foi {min(lista)}')
menor = 0
maior = 0
for x in range(1,6):
    peso = float(input(f'{[x]}Digite um peso:'))
    if x == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O Maior peso é de {maior} e o menor é {menor}')
