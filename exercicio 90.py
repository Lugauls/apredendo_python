#alunos = {'nome':[],'media':[]}
#alunos['nome'].append(str(input('Nome: ')).title())
#alunos['media'].append(float(input('Média: ')))
#if alunos['media'] < [7.0]:
    #print(f"O aluno {alunos['nome']} teve a média {alunos['media']} e foi reprovado")
#else:
    #print(f"O aluno {alunos['nome']} teve a média {alunos['media']} e foi aprovado")

aluno = {}
aluno['nome'] = str(input('Nome: ')).title()
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 7 :
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'  -{k} e igual a : {v}')