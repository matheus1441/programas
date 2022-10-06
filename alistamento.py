from datetime import date
atual=2022
ano=int(input('Digite o ano em que nasceu:'))
if (atual-ano)==18:
    print('Você deve se alistar JÁ')
elif (atual-ano)>18:
    x= (atual-ano)-18
    print('Você ja deveria ter se alistado há {} anos.' .format(x))
elif (atual-ano)<18:
    x= (atual-ano)-18
    print('Você deve se alistar em {} anos.'.format(x))
