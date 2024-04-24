import random
c = random.randint(1,10)
cont = 0
while True:
    e = str(input('Você é impar ou par?: ')).lower()
    if e == 'par':
        n = int(input('Digite um número:'))
        if (c+n) % 2 == 0:
            print('Você ganhou!')
            cont += 1
        elif (c+n) % 2 == 1:
            print('Você perdeu')
            break
    elif e != 'par' and e != 'impar':
        print('Opção incorreta')
        break
    else:
        n = int(input('Digite um número:'))
        if (c+n) % 2 == 1:
            print('Você ganhou!')
            cont += 1
        elif (c+n) % 2 == 0:
            print('Você Perdeu')
            break
print(f'Você ganhou {cont} vez/es')