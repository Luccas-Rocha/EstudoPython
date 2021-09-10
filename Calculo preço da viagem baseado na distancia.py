distancia = float(input('Digite a distancia da viagem em KM: '))

if distancia <= 200:
    preço = 0.5
if distancia >= 201:
    preço = 0.45

total = preço*distancia

print(f'o custo da viagem será de R${total:.2f}')
