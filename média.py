n1=float(input('Digite sua primeira nota:'))
n2=float(input('Digite sua segunda nota:'))
media=(n1+n2)/2
if media>=7:
    print('Parabéns, você foi APROVADO!')
elif media>=5 and media<7:
    print('Você está de RECUPERAÇÃO!')
else:
    print('Você está REPROVADO!')