valor=float(input('Qual o valor da casa?'))
salario=float(input('Qual seu salário?'))
tempo=int(input('Em quantos meses pretende pagar?'))
prestacao=valor/(tempo *12)
if prestacao<=(salario*30/100):
    print('Seu emprestimo foi aprovado! O valor da parcela será de R${:.2f}' .format(prestacao))
else:
    print('Seu emprestimo foi negado.')
