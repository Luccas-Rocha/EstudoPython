n1 = int(input('Digite um valor: '))
n2 = int(input('digite o outro: '))

escolha = 0

while escolha != 5:
    escolha = int(input('\no que você deseja fazer?\n'
                        '[1] somar\n'
                        '[2] multiplicar\n'
                        '[3] maior\n'
                        '[4] novos numeros\n'
                        '[5] sair do programa : '))
    if escolha == 1:
        soma = n1+n2
        print(f'\na soma foi de {soma}')
    if escolha == 2:
        multiplicação = n1*n2
        print(f'\na multiplicação foi de {multiplicação}')
    if escolha == 3:
        if n1 > n2:
            print(f'\no maior é {n1}')
        else:
            print(f'\no maior é {n2}')
    if escolha == 4:
        n1 = int(input('\nDigite um valor: '))
        n2 = int(input('\ndigite o outro: '))
