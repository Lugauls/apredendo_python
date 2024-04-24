from random import randint
computador = randint(0,10)
a = 0
acertou = False
while True:
    jogador= int(input('Digite um número(0/10):'))
    a+=1
    if jogador == computador:
        break
print(f'Acertou!,Você teve {a} palpites')
print(computador)
