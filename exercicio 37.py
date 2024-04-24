n = int(input('Digite 1 para binario\n2 para octal\n3 para hexadecimal\nQual sua escolha:'))
if n > 3:
    print('Escolha de 1, 2 ou 3, por favor!')
n2 = int(input('digite o número para ser transformado:'))
if n == 1:
    print(f'{n2} em binário é {bin(n2)[2:]}')
elif n == 2:
    print(f'{n2} em octal é {oct(n2)[2:]}')
else:
    print(f'{n2} em hexadecimal é {hex(n2)[2:]}')
