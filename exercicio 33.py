n1 = int(input('digite um número:')) #6
n2 = int(input('digite um número:')) #8
n3 = int(input('digite um número:')) #5
if n1>n2 and n2>n3:
    print(f'O {n1} é o maior número.')
elif n2>n3:
    print(f'O {n2} é o maior número.')
else:
    print(f'O {n3} é o maior número.')