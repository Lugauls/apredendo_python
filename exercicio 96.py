def terreno(l,c):
    t = l*c
    print("-="*30)
    print(f'A area de um terreno {l}x{c} é igual a : {t}m²')


print("  Controle de terrenos  ")
print("-="*30)
l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
terreno(l,c)