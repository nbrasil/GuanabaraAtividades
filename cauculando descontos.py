valor = float(input('Qual é o preço do produto? R$'))
desconto = valor - (valor * 0.05)
print(f'O produto que custava R${valor}, na promoção com desconto de 5% vai custar {desconto:.2f}.')
