lista = []
for x in range (0,5):
    num = int(input('Digite um número:'))
    lista += [num]
print(f'O maior número da lista é {max(lista)} e o menor é {min(lista)}')