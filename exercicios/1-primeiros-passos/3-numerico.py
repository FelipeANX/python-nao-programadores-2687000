data_nascimento = '05-10-1976'
idade_numerica = 46
altura = 1.74

# Descubra o tipo de dado de cada variável acima
print(type (data_nascimento))
print(type(idade_numerica))
print(type(altura))

# Realize uma operação entre dados do tipo string e inteiro
print (f"Quem nasce no ano de {data_nascimento} tem {idade_numerica} anos.")
print (data_nascimento+f" {idade_numerica} anos")
print (data_nascimento*idade_numerica)
# Realize uma operação entre dados do tipo inteiro e float
print (idade_numerica//altura)
print (idade_numerica/altura)
print (round((idade_numerica/altura),2))
