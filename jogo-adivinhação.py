from random import randint
nc = randint(0, 5)
print('---' * 20)
print("Estou pensando em um número de 1 a 5, tente adivinhar...")
print('---' * 20)
nj = int(input('Em que número eu pensei?'))
if nj==nc:
    print('Parabéns, você acertou')
else:
    print('O computador sempre vence.Pensei no {} e não no {}' .format(nc,nj))

