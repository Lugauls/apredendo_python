ficha = []
pessoa = {}
continuar = ''
media = soma = 0
while True:
    pessoa['nome']=(str(input('Nome: ')).title())
    while True:
        pessoa['sexo']=(str(input('Sexo: [M/F]')).upper()[0])
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Apenas M ou F')
        
    pessoa['idade']=(int(input('Idade: ')))
    soma += pessoa['idade'] 

    ficha.append(pessoa.copy())
    while True:
        continuar = str(input('Quer continuar:[S/N]')).upper()
        if continuar in 'SN':
            break
        print('ERRO! Apenas S ou N ')
    if continuar == 'N':
        break
media = soma / len(ficha)
print('-='*30)
print(f'A) O número de pessoas cadastradas são {len(ficha)}')
print(f'B)A média de idade é {media}')
print('C)As mulheres cadastradas São')
for p in ficha:
    if p['sexo'] in 'F':
        print(p['nome'])
print(f'D)Lista de pessoas que estão acima da media ')
for p in ficha:
    if p['idade'] >= media:
        print(f'{p["nome"]} = {p["idade"]}')
