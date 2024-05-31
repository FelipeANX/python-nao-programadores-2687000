# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input("Como é seu nome?")

# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = input("Você costuma estudar quantos dias por semana?")
total_dias = int(total_dias)
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas = input("Em média, você estuda quantas horas por dia?")
total_horas = int(total_horas)
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = input("Qual curso você está estudando?")
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
print (f"Boa noite, {nome}. Além de gostosa vi que você é estudante de {curso}, você tem estudado aproximadamente {total_horas*total_dias} horas por semana! Achei isso bem legal!! Te amo, {nome}!!")