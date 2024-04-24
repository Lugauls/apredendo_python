from math import *
catetooposto = float(input("digite o catetpo oposto: "))
catetoadjacente = float(input('digite o cateto adjacente: '))
hipotenusa = pow(catetooposto,2)+pow(catetoadjacente,2)
print (f'A hipotenusa é {sqrt(hipotenusa):.2f}')