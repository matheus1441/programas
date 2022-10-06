print('Bem vindo á sua Calculadora de números Reais Python')
print('Essas são as possíveis operações: \n 1-Soma \n 2-Subtração \n 3-Divisão \n 4-Multiplicação \n 5-Exponenciação \n 6-Divisão Inteira \n 7-Resto de Divisão')
op=input('Digite o número correspondente á operação:')
x=float(input('Digite o primeiro número:'))
y=float(input('Digite o segundo número:'))
d=float(x/y)

if op==1 : print('Resultado:',x+y)

elif op==2 : print("Resultado:", x-y)

elif op==3 : print('Resultado', d)

elif op==4 : print('Resultado',x*y)

elif op==5 : print('Resultado',x**y)

elif op==6 : print('Resultado',x//y)

else : print("Resultado", x%y) 





