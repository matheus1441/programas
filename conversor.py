num=int(input('Digite um numero inteiro:'))
print('Escolha uma das bases para a conversão:[1] para BINARIO    [2] para OCTAL    [3] para HEXADECIMAL')
escolha=int(input('Digite o numero correspondente a escolha:'))
if escolha==1:
    print('Resultado: {}' .format(bin(num)))
elif escolha==2:
    print('Resultado: {}' .format(oct(num)))
elif escolha==3:
    print('Resultado: {}' .format(hex(num)))
else:
    print('Opção invalida. Tente novamente.')
