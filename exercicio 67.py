while True:
    n = int(input('Qual tabuada você quer ver:'))
    print('-='*10)
    if n < 0:
        print('Opção Inválida')
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    