import datetime
x = datetime.datetime.now()
cadastro = {}
cadastro['nome'] = str(input('Nome: ')).title()
cadastro['idade'] = x.year - int(input('Ano de nascimento: ')) 
cadastro['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['carteira'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: '))
    cadastro['aposentadoria'] =  (cadastro['idade']+(cadastro['contratação'] +35)- x.year)
    
    for k,v in cadastro.items():
        print(f' {k} tem valor : {v}')
    
    #print(f'O nome é {cadastro["nome"]}')
    #print(f'A idade tem valor : {cadastro["idade"]}')
    #print(f'Cpts tem valor : {cadastro["carteira"]}')
    #print(f'O ano de contratação é {cadastro["contratação"]}')
    #print(f'O salario é igual a : {cadastro["salario"]}')
    #print(f'O ano da aponsetadoria é igual a : {cadastro["aposentadoria"]}')


if cadastro['carteira'] == 0:
    for k,v in cadastro.items():
        print(f' {k} tem valor : {v}')
    
    #print(f'O nome é {cadastro["nome"]}')
    #print(f'A idade tem valor : {cadastro["idade"]}')
    #print(f'Cpts tem valor : {cadastro["carteira"]}')


