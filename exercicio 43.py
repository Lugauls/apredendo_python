from math import pow
p = float(input('Digite seu peso: '))
a = float(input('digite sua altura: '))
imc = p/(pow(a,2))
if imc <18.5:
    print('Voce está abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
    print('Voce está no peso ideal.')
elif imc > 25 and imc <= 30:
    print('Voce está um pouco acima do peso.')
elif imc > 30 and imc <= 40:
    print('Voce está obeso!')
else:
    print('é obesidade morbida, procure um medico')