n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m < 5.0:
    print('MUITO BURRO, REPROVADO!')
elif m > 5.0 and m < 7:
    print('MEIO BURRO, RECUPERAÇÃO!')
else:
    print('Legal, tu passou')