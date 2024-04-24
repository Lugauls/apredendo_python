v = int(input('Digite a velocidade atual do carro:'))
if v > 80:
    print(f'Voce foi multado em {(v-80)*7} reais!')
else:
    print('Pode seguir em frente')