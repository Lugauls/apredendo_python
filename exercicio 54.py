import datetime
x = datetime.datetime.now()
maiores = 0
menores = 0
for a in range(1,8):
    ano = int(input(f'{[a]}Digite o ano do seu nascimento: '))
    if (x.year - ano) < 18:
        menores += 1
    else:
        maiores += 1
print(f'O número de pessoa maiores de idade é {maiores}\nE os de menores é {menores}')
