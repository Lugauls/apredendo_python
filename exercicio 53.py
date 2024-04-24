frase = input('Digite uma frase: ').lower().strip()
#frase.replace(' ', '')
fraseNova = ''

for i in range(len(frase),0,-1):

    fraseNova += frase[i-1]

if frase == fraseNova:
    print('É palindromo')

else:
    print("Não é palíndromo")