n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite a razão da PA: '))
c = 0
print('Os 10 primeiros termos da PA são:')
while c < 10:
    print(n1, end=' ')
    n1 += n2
    c += 1
n3 = int(input('\nMais algum número: '))
if n3 > 0:
    print('Os outros termos são:')
    for x in range(0,n3):
        print(n1, end=' ')
        n1 +=n2
else:
    print('Fim')

