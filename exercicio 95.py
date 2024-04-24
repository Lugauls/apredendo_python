jogadores = []
ficha = {}
while True:
    ficha['nome']= str(input('Nome do jogador:')).title()
    ficha['gols'] = []
    
    partidas = int(input('Quantas partidas ele jogou: '))
    
    for c in range(0,partidas):
        ficha['gols'].append(int(input(f'Quantos gols na partida {c+1}: ')))
    
    ficha['total'] = sum(ficha['gols'])
    
    jogadores.append(ficha.copy())
    
    while True:
        continuar = str(input('Quer continuar:[S/N]')).upper()
        if continuar in 'SN':
            break
        print('ERRO! Apenas S ou N')
    if continuar in 'N':
        break

print("-="*30)
print(f"{'Cod':<4} {'Nome':<10} {'Gols':<7}")
print('-='*30)
for i,j in enumerate(jogadores):
    print(f"{i:<4} {j['nome']:<10} {j['gols']} Total : {j['total']}")
print('-='*30)

while True:
    opc = int(input('Mostrar dados de qual jogador?:[999 para interromper]'))
    if opc == 999:
        break
    if opc <= len(jogadores):
        print(f'Mostrando dados de {jogadores[opc]["nome"]}')
        for j,g in enumerate(jogadores[opc]['gols']):
            print(f'No jogo {j} fez : {g}')

