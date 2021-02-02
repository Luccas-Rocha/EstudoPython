preço = float(input('digite o preço do produto: R$ '))
forma = int(input('digite a forma de ser pago\n1 = à vista dinheiro/check: 10% de desconto\n'
                  '2 = à vista no cartão: 5% de desconto\n'
                  '3 = em até 2x no cartão: preço normal\n'
                  '4 = 3x ou mais no cartão: 20% de juros'))

if forma == 1:
    preço = preço * 0.9
    print(f'o preço final ficou de R${preço:.2f}')
elif forma == 2:
    preço = preço * 0.95
    print(f'o preço final ficou de R${preço:.2f}')
elif forma == 3:
    print(f'o preço final ficou de R${preço:.2f} em 2x de {preço/2}')
elif forma == 4:
    vezes = int(input('em quantas vezes deseja pagar?: '))
    preço = preço * 1.20
    print(f'o preço final ficou de R${preço:.2f} em {vezes}x de {preço/vezes}')
