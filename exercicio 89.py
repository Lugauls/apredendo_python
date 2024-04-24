ficha = []
alunos = []
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2)/2
    alunos.append(nome)
    alunos.append(media)
    alunos.append([nota1,nota2])
    ficha.append(alunos[:])
    alunos.clear()
    continuar = str(input('Deseja continuar?[S/N]:')).upper()
    if continuar == 'N' or continuar != 'S':
        break

print(f"{'n°':<4} {'nome':<10} {'media':>8} ")
for i,a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[1]:>8.1f} ')
while True:
    opc = int(input('Qual aluno você quer ver? [999 para interromper]: '))
    if opc == 999:
        break   
    if opc <= len(ficha)-1 :
        print(f'As notas de {ficha[opc][0]} são {ficha[opc][2]}') 