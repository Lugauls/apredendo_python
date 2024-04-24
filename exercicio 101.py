def votaçao(num):

    import datetime
    x = datetime.datetime.now()
    idade = x.year - num
    if idade < 16:
        return f'Com {idade} não vota.'
    elif idade <= 16 or idade < 18 or idade > 65:
        return f'Com {idade} o voto é opcional.'
    else:
        return f'Com {idade} o voto é obrigatório. '

nasc = int(input('Digite sua data de nascimento: '))
print(votaçao(nasc))

