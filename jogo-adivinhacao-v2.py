cont=0
nj=0
from random import randint
nc=randint(0, 10)
print('---' * 20)
print("Estou pensando em um número de 1 a 10, tente adivinhar...")
print('---' * 20)

while not nj==nc:
    nj=int(input('Qual número estou pensando?'))
    cont+=1
    if nj==nc:
        print('Parabéns, você acertou em {} tentativas.'.format(cont))
    else:
        if nj<nc:
            print('Tente um número maior...')
        elif nj>nc:
            print('Tente um número menor...')


