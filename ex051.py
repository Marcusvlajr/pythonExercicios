"""Desenvolva um programa que leia o primeiro termo e a razao de uma PA.
No final, mostre os 10 primeiros termos dessa progressao."""

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao'))
decimo = primeiro + (10 - 1) * razao
for c in range( primeiro, decimo, razao):
    print('{}'.format(c), end=' > ')
print('ACABOU.')