from random import randint
from time import sleep
print('######### JOGO DA ADVINHAÇÃO #######')
numero = int(input('Advinhe um número entre 0 e 5: '))
pc = randint(0, 5)
print('Processando...')
sleep(2)
if numero == pc:
    print('Você acertou o número, o número escolhido é {} ! MEUS PARABÉNS !!!!'.format(pc))
else:
    print('Você errou o número, o número escolhido era {} ! TENTE DE NOVO'.format(pc))
