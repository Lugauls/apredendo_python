a = int(input('Digite um número: '))
b = 1
if a < 10 :
        b = 0
for n in range(1,10):
    if a % n == 0:
        b += 1
if b>2:
    print(f'O número {a} não é primo pois ele é divido {b} vezes')
else:
    print(f"O número {a} é primo pois ele é divido {b} vezes.")
