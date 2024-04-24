homem = ''
hv = 0
somaida= 0
maioridadeh = 0
idademulher = 0
for x in range(1,5):
    print("-="*10)
    n = str(input('Digite seu nome:'))
    i = int(input('Digite sua idade: '))
    s = str(input('digite seu sexo(M/F): ')).upper()
    print("-="*10)
    if x == 1 and s == 'M':
        maioridadeh = i
        hv = n
    if s == 'M' and i > maioridadeh:
        maioridadeh= i
        hv = n
    if s == 'F' and i<20:
        idademulher += 1

    somaida += i
mediaida = somaida/4
print(f"A média de idade do grupo é {mediaida}")
print(f'O nome do homem mais velho é {hv} e a idade dele é {maioridadeh}')
print(f'Tem {idademulher} abaixo de 20 anos')