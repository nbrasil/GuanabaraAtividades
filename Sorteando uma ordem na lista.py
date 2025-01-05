import random

primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')

alunos = [primeiro, segundo, terceiro, quarto]
lista = random.shuffle(alunos)
print(f'A ordem de exibição da lista será: {alunos}')