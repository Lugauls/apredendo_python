cont = 1
n = int(input('Digite um número: '))
maior = n
menor = n
soma = n
while True :
    a = str(input('Quer continuar?[S/N]:')).lower()
    if a =='n':
        break
    elif a != 's' and a != 'n':
        print('opção errada!')
        break
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = (soma/cont)
print(f'Você digitou {cont} números e a média deles é {media}')
print(f'O maior número {maior} e o menor é {menor}')