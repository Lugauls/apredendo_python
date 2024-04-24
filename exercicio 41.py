import datetime
n = int(input('Digite o ano do seu nascimento: '))
x = datetime.datetime.now()
if (x.year - n) <= 9:
    print('Voce está na categoria mirim da natação.')
elif(x.year - n) > 9 and (x.year - n) <= 14:
    print('Voce está na categoria infantil da natação.')
elif(x.year - n) > 14 and (x.year - n) <= 19:
    print('Voce está na categoria junior na natação.')
elif(x.year - n) == 20:
    print('Voce está na categoria sênior da natação.')
else:
    print('Voce está na categoria Master da natação.')