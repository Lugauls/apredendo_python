v = int(input('digite a distancia da viagem em km: '))
if v > 200:
    print(f'O valor da passagem fica: ${v*0.45}')
else:
    print(f'O valor da passagem fica: ${v*0.50}')
