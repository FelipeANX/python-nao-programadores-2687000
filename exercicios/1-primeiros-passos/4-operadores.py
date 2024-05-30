ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
idade_formatura = (ano_formatura-ano_nascimento)
print (idade_formatura)

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
idade_hoje=(2024-ano_nascimento)
print (idade_hoje > idade_formatura)
print (ano_formatura <= ano_nascimento)
print (idade_formatura==21)

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
print (idade_hoje > idade_formatura and idade_formatura < 46)