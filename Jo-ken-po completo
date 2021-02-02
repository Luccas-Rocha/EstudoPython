from time import sleep
from random import randint
print('Vamos jogar JOKENPÔ, digite a sua jogada')
escolhaplayer = int(input('1 = Papel\n'
                    '2 = Pedra\n'
                    '3 = Tesoura: '))

escolhacomputador = randint(1,3)

if escolhaplayer == 1:
    print('você escolheu Papel.')
    resultador = escolhaplayer + escolhacomputador
    if resultador == 2:
      sleep(2)
      print('eu também escolhi Papel, empatamos!')
    elif resultador ==3:
        sleep(2)
        print('eu escolhi Pedra e você Papel, você ganhou!')
    elif resultador == 4:
        sleep(2)
        print('eu escolhi Tesoura e você Papel, eu ganhei!')
if escolhaplayer == 2:
    print('Você escolheu Pedra.')
    resultador = escolhaplayer + escolhacomputador
    if resultador == 3:
        sleep(2)
        print('eu escolhi Papel e você Pedra, eu ganhei!')
    elif resultador == 4:
        sleep(2)
        print('eu também escolhi Pedra, empatamos!')
    elif resultador == 5:
        sleep(2)
        print('eu escolhi Tesoura e você pedra, você ganhou')
if escolhaplayer ==3:
    resultador = escolhaplayer+escolhacomputador
    if resultador == 4:
        sleep(2)
        print('eu escolhi Papel e você Tesoura, você ganhou')
    elif resultador == 5:
        sleep(2)
        print('eu escolhi Pedra e você Tesoura, eu ganhei!')
    elif resultador == 6:
        sleep(2)
        print('eu também escolhi Tesoura, empatamos!')
