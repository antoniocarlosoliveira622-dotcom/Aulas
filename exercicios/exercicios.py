# Exercício 1: Calculadora de Comissão

# Cenário de Vendas: Você acabou de fechar um negócio e quer calcular rapidamente sua 
# comissão de 25%. 

# input -> perguntar
# print -> mostrar

# [colchetes] - listas ou arrays 
# {chaves} - objetos
# (parenteses) - funcoes

# 1. Entrada dos dados
# valor_venda = float(input("Digite o valor total da venda: R$:"))

# 2. Processamento
# taxa_comissao = 0.25
# comissao = valor_venda * taxa_comissao

# 3. Saida
# print('O valor da sua comissão foi ', comissao)
# print(f"Sua comissão de 25% é: R$ {comissao:.2f}")

# O que fazer: Crie um programa que receba o valor total da venda e mostre o valor da sua comissão. 

# --------
# Exercício 2: Média de Vendas do Trimestre
# Cenário de Vendas: Seu gestor pediu a média do valor das suas últimas 3 
# vendas para a reunião trimestral.


# O que fazer: Faça um programa que receba o valor de três vendas, 
# calcule e mostre a média aritmética entre elas. 
# primeira_venda = int(input("qual foi o valor da primeira venda" ))
# segunda_venda = int(input("qual foi o valor da segunda venda" ))
# terceira_venda = int(input("qual foi o valor da terceira venda" ))

# calcule
# soma os valores e dividir pelo numero de vendas
# media_aritmetica = (primeira_venda + segunda_venda + terceira_venda) / 3

# Operadores aritmeticos
# + soma
# - subtração
# * multiplicacao
# / divisão

# mostre
# print("A média das vendas foi", media_aritmetica)
# ------
# Exercício 3: Alerta de Grande Negócio
# Cenário de Vendas: Na sua empresa, qualquer venda acima de R$ 50.000,00 
# precisa de uma aprovação extra do seu gestor. Você quer criar um alerta para 
# não se esquecer.
# O que fazer: Crie um programa que recebe o valor de uma venda e, se o valor for maior que 50.000, exibe a mensagem "ALERTA: Negócio precisa de aprovação do gestor!". 
# (Baseado no exercício da multa de velocidade ).
# 1. Entrada de Dados
# valor_negocio = float(input("Qual o valor do negócio fechado? R$ "))


# 2. Estrutura de Decisão Simples
# A condição é verificar se o valor é superior a 50.000,00
# if(valor_negocio > 50000):
#       print ("alerta de venda acima de R$ 50.000.00 ")

# print ("alerta de venda acima de 50.001.00 negocio precisa de aprovaÇão do gestor")

# Exercício 4: Política de Descontos Automática
# Cenário de Vendas: Sua empresa tem uma política de preços inteligente. 
# Para produtos cujo custo de aquisição é menor que R$ 200,00, a margem de lucro é de 45%. 
# Para custos iguais ou maiores que R$ 200,00, a margem é de 30%, pois são itens de maior giro.

# O que fazer: Crie um programa que receba o custo de um produto e calcule o preço final de venda com base nessa regra. 

custo_produto_1 = 199.00
custo_produto_2 = 200.00

if(custo_produto_1 < 200.00):
      preco_venda = custo_produto_1 * 1.45
else:
      preco_venda = custo_produto_1 * 1.30

print('O preço de venda sugerido é: R$ ', preco_venda)

if(custo_produto_2 < 200.00):
      preco_venda = custo_produto_2 * 1.45
else:
      preco_venda = custo_produto_2 * 1.30

print('O preço de venda sugerido é: R$ ', preco_venda)

# print("199.00 este é valor do produto com margem o preço final é de 286.00")
# print("201.00 este é o valor do produto, o comerciante terá um lucro de 261.00 este será o preço final do comerciante")