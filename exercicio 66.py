cont = 0
soma = 0
while True:
    n = int(input('Digite um número[999 para sair]:'))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} números e a soma deles é {soma}')