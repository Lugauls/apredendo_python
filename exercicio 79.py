lista = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
    continuar = str(input('Voce quer continuar[S/N]?: ')).upper()
    if continuar == "N":
        break
    elif continuar != 'S' and continuar != 'N':
        print('Opção invalida')
        break
lista.sort()
print(f'Os números da lista são {lista}')
