m = str(input('qual é seu sexo?(M/F): ')).upper()
while m not in 'MF':
    m = str(input('Opção invalida, Digite novamente:')).upper()
print('FIM')