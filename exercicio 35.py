print('Os números a seguir podem fazer um triangulo?')
r1 = int(input('Digite um número:'))
r2 = int(input('Digite um número:'))
r3 = int(input('Digite um número:'))
if (r2-r3)<r1<(r2+r3) and (r1-r3)<r2<(r1+r3) and (r1-r2)<r3<(r1+r2):
    print('Sim,esses números podem fazer um triangulo')
else:
    print('Não, esses números não podem fazer um triangulo')