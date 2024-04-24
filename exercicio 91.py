from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
jogadores['jogador 1'] = randint(1,6)
jogadores['jogador 2'] = randint(1,6)
jogadores['jogador 3'] = randint(1,6)
jogadores['jogador 4'] = randint(1,6)
ranking = []

sorted(jogadores)
for k,y in jogadores.items():
    print(f'O {k} recebe : {y}')
    sleep(1)
ranking = sorted(jogadores.items(),key=itemgetter(1),reverse=True)
print('-='*30)
for i,v in enumerate(ranking):
    print(f'{i+1}° lugar : {v[0]} com {v[1]}')
    sleep(1)