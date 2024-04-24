from time import sleep

def contagem(i,f,p):
    linha()
    print(f'Contagem de {i} a {f} de {p} em {p}')
    
    if i < f :
        cont = i
        while cont <= f :
            print(f'{cont}',end=' ',flush=True)
            sleep(0.5)
            cont += p
        print('Fim!')
        linha()
    else:
        cont = i
        while cont >= f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.5)
            cont -= p
        print('Fim!')
        linha()

def linha():
    print('-='*30)

contagem(1,10,1)
contagem(10,2,2)
print('Agora é a sua vez')
sleep(0.5)
i = int(input('Inicio: '))
f = int(input('Fim:'))
p = int(input('Passo:'))
contagem(i,f,p)



