lista = []
listaim = []
listapa = []
while True:
    num = int(input('Digite um número:'))
    lista += [num]
    if num % 2 == 0 :
        listapa += [num]
    else:
        listaim += [num]
    continuar = str(input('Quer continuar?[S/N]')).upper()
    if continuar == 'N' or continuar != 'S':
        break
print(f'Os números digitados foram {lista}')
print(f'Os números ímpares são {listaim}')
print(f'Os números pares são {listapa}')