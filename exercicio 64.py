p = 0
c = 0
soma = 0
while p != 999:
    p = int(input('Digite alguns número[999 para parar]:'))
    c += 1
    soma += p
print(f'Você digitou {c-1} números e a soma deles foi {soma - 999}')