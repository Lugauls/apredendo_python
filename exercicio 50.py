s = 0
for c in range(0,6):
    a = int(input('Digite um número:'))
    if a % 2 == 0:
        s += a
print(f'A soma dos números pares é {s}')