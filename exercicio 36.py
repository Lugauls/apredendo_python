c = int(input('digite o valor da casa: ')) #200k
s = int(input('digite o valor do salário: ')) #1k
a = int(input('digite em quantos anos vai ser pago: ')) #50
p = c/(a*12)
if p > (s*30)/100:
    print('Não é possivel comprar essa casa, sinto muito.')
else:
    print(f'É possivel comprar essa casa o valor da prestação é : ${p:.2f}')