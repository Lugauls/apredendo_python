print('='*30)
print('Banco de birilai')
print('='*30)
valor= int(input('Digite um valor: '))
cedula = 50
total = valor
totalced = 0
while True:
    if total >= cedula:
        total -= cedula
        totalced += 1
    else:
        if totalced > 0:
            print(f'O total de cedulas é {totalced} de R${cedula} ')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if total == 0:
            break