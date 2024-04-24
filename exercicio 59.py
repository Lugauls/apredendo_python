n1 = input('Digite o primeiro valor: ')
while n1.isdigit() == False:
    print('Digite um número, por favor.')
    n1 = input('Digite o primeiro valor: ')

n2 = input('Digite o segundo valor: ')
while n1.isdigit() == False:
    print('Digite um número, por favor.')
    n2 = input('Digite o segundo valor: ')

n1 = int(n1) 
n2 = int(n2)  
    
continuar = True

while continuar:
    print('-='*10)
    escolha = input('''[1]Soma
[2]Multiplicar
[3]Subtração
[4]Divisão
[5]Novos números
[6]Sair
Qual é a escolha: ''')
    print('-='*10)
    
    while escolha.isdigit() == False:
        print('Por favor, escolha uma das opções abaixo')
        print('-='*10)
        escolha = input('''[1]Soma
[2]Multiplicar
[3]Subtração
[4]Divisão
[5]Novos números
[6]Sair
Qual é a escolha: ''')
        print('-='*10)


    escolha = int(escolha)

    if escolha == 1:
        print(f'A soma de {n1} e {n2} é : {n1+n2}')
    
    elif escolha == 2:
        print(f'A multiplicação de {n1} e {n2} é : {n1*n2}')
    
    elif escolha == 3:
        print(f'A subtração de {n1} e {n2} é : {n1-n2}')

    elif escolha == 4:
        print(f'A Divisão de {n1} e {n2} é : {n1/n2}')

    elif escolha == 5:
        n1 = input('Digite o primeiro valor: ')
        while n1.isdigit()== False:
            print('Digite um número, por favor.')
            n1 = input('Digite o primeiro valor: ')

        n2 = input('Digite o segundo valor: ')
        while n1.isdigit()== False:
            print('Digite um número, por favor.')
            n2 = input('Digite o segundo valor: ')
        
        n1 = int(n1)
        n2 = int(n2)

    elif escolha == 6:
        print('Obrigador por usar.')
        continuar = False
        #Colocar break funcionaria tambem
    
    else:
        print('Opção incorreta, escolha uma certa')       