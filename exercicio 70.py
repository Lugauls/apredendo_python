cont = total = mil = menor = 0
barato = ''
while True:
    produto = str(input('Qual o nome do produto: '))
    preço = float(input('Qual preço do produto:'))
    cont += 1
    if cont == 1 :
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
    if preço > 1000:
        mil += 1
    total += preço
    continuar = str(input('Voce quer continuar[S/N]?:')).upper()
    if continuar == "N":
        break
    if continuar != "N" and continuar != "S":
        print('Opção ínvalida.')
        break
print(f'''O total gasto é de R${total}
Tem {mil} produto(s) acima de R$1000
O preço mais baixo é {menor} e é da(o) {barato} ''')