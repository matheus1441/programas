s=0
for c in range(1,500+1,2):
    if c%3==0:
        s=s+c
print('A soma de todos os multiplos de 3 entre 1 e 500 é {}.' .format(s))
print('FIM')
