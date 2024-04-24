lista = []
cont = 0
while True:
    num = int(input('Digite um número: '))
    lista += [num]
    cont += 1
    resp = str(input('Voce quer continuar[S/N]:')).upper()
    if resp == 'N' or resp != 'S':
        break
lista.sort(reverse=True)
print(f'Foram Digitados {cont} números')
print(f'A lista em ordem decrescente é {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')