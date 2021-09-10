data = int(input('Digite o ano de nascimento: '))

requisito = (2021 - data)
check = -(requisito - 18)

if check < 0:
   check = check * -1

if requisito == 18:
    print('esse é o ano de alistamento.')
elif requisito < 18:
    print(f'você só precisará se alistar daqui {check} ano(s)')
elif requisito > 18:
    print(f'o tempo de alistar já passou faz {check} ano(s)')
