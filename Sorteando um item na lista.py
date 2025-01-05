from random import choice

primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')

alunos = choice([primeiro, segundo, terceiro, quarto])
print(f'O aluno escolhido foi: {alunos}')

