def jogador():
    nome = input("Qual nome do jogador: ").title()
    gols = input("Quantos gols ele fez:  ")
    if nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric == True:
        gols = int(gols)
    else:
        gols = 0

    print(f"O {nome} fez {gols} no campeonato")

jogador()