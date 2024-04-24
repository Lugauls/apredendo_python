print('Os números a seguir podem fazer um triangulo?')
r1 = int(input('Digite um número:'))
r2 = int(input('Digite um número:'))
r3 = int(input('Digite um número:'))
if (r2-r3)<r1<(r2+r3) and (r1-r3)<r2<(r1+r3) and (r1-r2)<r3<(r1+r2):
    if r1 == r2 == r3:
        print('''Sim,esses números podem fazer um triangulo')
Esses números fazem um triangulo Equilátero''')
    elif r1 == r2 or r1 == r3 or r2== r3:
        print('''Sim,esses números podem fazer um triangulo')
Esses números fazem um triangulo isóceles''')
    else:
        print('''Sim,esses números podem fazer um triangulo
esses números fazem um triangulo Escaleno''')
else:
    print('Esses números não fazem um triangulo')