n = int(input('Quantos termos da Sequencia de Fibonacci você quer ver:'))
c = 1
t1 = 0
t2 = 1
while c <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    c += 1
    print(t3)