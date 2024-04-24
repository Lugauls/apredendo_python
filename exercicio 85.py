numeros = [[],[]]
for x in range(1,8):
    valor = int(input(f'Digite o {x}° número: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares são {numeros[0]}')
print(f'Os números impares são {numeros[1]}')