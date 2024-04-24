lista = []
pos = 0
for c in range(0,5):
    num = int(input('Digite um número:'))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('O número foi Adicionado na ultima posição')
    else: 
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos , num)
                print(f'O número foi adicionado na posição {pos} ')
                break
            pos += 1
print('-='*30)
print(f'Os números na lista são {lista}')