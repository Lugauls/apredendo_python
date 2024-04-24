import datetime
n = int(input('Digite o ano do seu nascimento: '))
x = datetime.datetime.now()
if(x.year - n) == 18 :
    print('Voce precisa se alistar, desempregado!')
elif(x.year - n) < 18:
    print(f'Voce ainda não pode se alistar, falta {18 - (x.year - n)} ano(s)')
else:
    print(f'Voce está atrasado em {(x.year - n) - 18} ano(s), vá se alistar.')