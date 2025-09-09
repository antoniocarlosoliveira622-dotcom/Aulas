print("Olá, Mundo!") # para escrever no terminal

print(10 + 5)

# Variáveis: As Gavetas de Informação do Cliente

# Para isso, usamos as  variáveis, que são espaços na memória do computador rotulados 
# com um nome para guardar valores

nome_cliente = "Empresa ABC"
valor_oportunidade = 50000
etapa_funil = "Negociação"

# Para organizar as informações, precisamos saber qual o tipo de dado estamos guardando. 
# Os tipos mais comuns em Python são:


# Números Inteiros: Números sem parte fracionária.

# Analogia: quantidade_licencas = 10


# Números de Ponto Flutuante (Reais): Números com parte decimal.

# Analogia: comissao_venda = 4550.75


# Strings: Sequência de caracteres (letras, números, símbolos). Usamos para textos.

# Analogia: email_contato = "contato@empresaabc.com.br"

# Lógico (Booleano): Representa apenas dois valores, Verdadeiro (True) ou Falso (False).

# Analogia: decisor_contatado = True

# 3. input() - Conversando com seu Programa
# Para conseguir obter informações do usuario

nome_usuario = input("Qual é o seu nome?")
print("Olá," + nome_usuario + "! Seja bem-vindo(a)!")