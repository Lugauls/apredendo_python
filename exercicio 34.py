s =float(input('Digite o salário do funcionario: '))
a = (s*10)/100
b = (s*15)/100
if s > 1250:
    print(f'O aumento do salário é de ${s+a}')
else:
    print(f'O aumento do salário é de ${s+b} ')