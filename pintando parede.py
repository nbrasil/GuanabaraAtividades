largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
mq = largura * altura
tinta = mq / 2
print(f'Sua parede tem a dimensão de {largura}x{altura} e a sua área é de {mq}m².\n'
      f'Para pintar essa parede, você precisará de {tinta}L de tinta.')