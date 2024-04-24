a = ('zero','um','dois','tres','quatro','cinco','seis','sete','nove','nove','dez'
,'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 20:
        num = int(input('Tente novamente, entre 0 e 20: '))
    print(f'O número digitado foi {a[num]} ')
    continuar = str(input('Voce quer continuar[S/N]: ')).upper()
    if continuar == 'N':
        break
    else:
        if continuar != "S":
            break