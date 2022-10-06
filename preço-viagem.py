d=float(input('Digite a distancia em KM de sua viagem:' ))
if d<200:
    print('Sua passagem custa R${}' .format(d*0.5))
else:
    print('Sua passagem custa R${}' .format(d*0.45))
    