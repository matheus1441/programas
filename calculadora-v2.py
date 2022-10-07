n1=float(input('Digite o primeiro valor:'))
n2=float(input('Digite o segundo valor:'))
opcao=0
while opcao !=7:
    print('''[1] SOMAR
    [2] SUBTRAIR
    [3] MULTIPLICAR
    [4] DIVISÃO
    [5] MAIOR
    [6] NOVOS NÚMEROS
    [7] SAIR
    ''')
    opcao=int(input('Qual a operação desejada?'))
    if opcao==1:
        print('---'*10)
        print('RESULTADO:{}'.format(n1+n2))
        print('---'*10)
    elif opcao==2:
        print('---'*10)
        print('RESULTADO:{}'.format(n1-n2))
        print('---'*10)
    elif opcao==3:
        print('---'*10)
        print('RESULTADO:{}'.format(n1*n2))
        print('---'*10)
    elif opcao==4:
        print('---'*10)
        print('RESULTADO:{}'.format(n1/n2))
        print('---'*10)
    elif opcao==5:
        if n1>n2:
            print('---'*10)
            print('O valor {} é maior.'.format(n1))
            print('---'*10)
        else:
            print('---'*10)
            print('O valor {} é maior.'.format(n2))
            print('---'*10)
    elif opcao==6:
        print('---'*10)
        n1=float(input('Digite o primeiro valor:'))
        n2=float(input('Digite o segundo valor:'))
print('FIM DO PROGRAMA')