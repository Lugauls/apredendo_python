import random
from time import sleep

#numeros = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
#print('-='*30)
#contador = int(input('Quantos números serão sorteados?: '))
#for x in range(1,contador+1):
    #print(f'{x}°jogo:{sorted(random.sample(numeros,k=6))} ')
#    sleep(1)

jogos = []
lista = []
quant = int(input('Quantos jogos seram sorteados: '))
totquant = 1
while totquant <= quant:
    cont = 0 
    while True:
        num = random.randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totquant += 1
for i,l in enumerate(jogos):
    print(f'jogo {i+1} é: {l}')
    sleep(1)
