h = 0
m = 0
maior = 0
while True:
    print('Cadastre uma pessoa ')
    a=int(input('Idade: '))
    b=str(input('Sexo[M/F]: ')).upper()
    if a <= 18:
        maior += 1
    if a < 0:
        print('Opção invalida')
        break
    if b == 'M':
        h += 1
    if  b == 'F' and a < 18:
        m  += 1
    if b != "M" and b != "F":
        print ('Opção incorreta.')
        break
    c=str(input('Quer continuar[S/N]?:')).upper()
    if c == 'N':
        break
print(f'''O número de maiores de idade é {maior}
O número de homens é {h}
O número de Mulheres menores de 18 é {m} ''')
