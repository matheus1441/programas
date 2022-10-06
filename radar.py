vl=float(input('Qual a velocidade limite da via?'))
v=float(input('Qual é a velocidade atual do carro?'))
if v>vl:
    multa= (v-vl) * 7
    print('Você está acima do limite, foi multado em R${:.2f}!' .format(multa))
else:
    print('Você está dentro do limite da via. Dirija com segurança.')