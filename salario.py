s=float(input('Digite seu salário:'))
if s<= 1250:
    print('Seu salário reajustado será R${}' .format(s+(s*15/100)))
else:
    print('Seu salário reajustado será R${}' .format(s+(s*10/100)))
