frase = input('Digite uma frase: ').upper().strip()
a = frase.count('A')
f = frase.find('A')+1
u = frase.rfind('A')
print (f"A letra 'A' apareceu: {a} vezes")
print (f"A letra 'A' apareceu na posiçao: {f}")
print(f"A letra 'A' apareceu pela ultima vez em: {u} ")