jogador = {}
jogador['nome'] = str(input('Nome do jogador: ')).title()
jogador['gols'] = []
partidas = int(input('Quantas partidas ele jogou: '))
for j in range(0,partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {j+1}: ')))
jogador['total'] = sum(jogador['gols'])
print('-='*30)
print(jogador)

print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem valor {v}')

print('-='*30)
print(f'Jogador {jogador["nome"]} jogou {partidas} partidas')
for j,g in enumerate(jogador['gols']):
    print(f'--> Na partida {j+1}, fez {g} ') 
print(f'No total foram {jogador["total"]} gols')
