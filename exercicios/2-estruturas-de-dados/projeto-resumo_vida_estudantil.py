# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
estudante = {}
estudante ['nome'] = input('Qual é o seu nome? ')
estudante ['ano_faculdade'] = int(input('Em que ano você começou a facultade? '))
estudante ['curso'] = input('Qual curso você fez? ')
estudante ['ano_atual'] = int(input('Qual é o ano atual?'))
estudante ['materias'] = input('Quais foram suas 5 matérias favoritas? (separe elas com vírgulas em ordem de favorita)')
estudante ['formacao'] = int(input('Qual ano da sua formação?'))

# 2. Armazene esses dados em um dicionário
estudante ['materias'] = materias.split(', ')

# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
print(f'Oi, {estudante['nome']}, já estamos em {estudante["ano_atual"]} e fazem {estudante["ano_atual"]-estudante["formacao"]} anos que você se formou no curso de {estudante["curso"]}. Nos {estudante["formacao"]-estudante["ano_faculdade"]} anos de curso você gostou muito de ter feito as matérias de {estudante["materias"]}! Mas a favorita foi {estudante["curso"][0]}. Já parou para pensar no motivo dessa escolha?')