from random import randint
def sortear(lista):
    for cont in range(0,5):
        lista.append(randint(0,10))

def somapar(num):
    pares = 0
    for p in num:
        if p % 2 == 0:
            pares += p
    print(f'A soma dos pares é {pares}')
            


numeros = []
sortear(numeros)
print(numeros)
somapar(numeros)


