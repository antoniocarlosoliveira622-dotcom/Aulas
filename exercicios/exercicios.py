# Exercício 1: Calculadora de Comissão

# Cenário de Vendas: Você acabou de fechar um negócio e quer calcular rapidamente sua 
# comissão de 25%. 

# input -> perguntar
# print -> mostrar

# [colchetes] - listas ou arrays 
# {chaves} - objetos
# (parenteses) - funcoes

# 1. Entrada dos dados
valor_venda = float(input("Digite o valor total da venda: R$:"))

# 2. Processamento
taxa_comissao = 0.25
comissao = valor_venda * taxa_comissao

# 3. Saida
print('O valor da sua comissão foi ', comissao)
# print(f"Sua comissão de 25% é: R$ {comissao:.2f}")

# O que fazer: Crie um programa que receba o valor total da venda e mostre o valor da sua comissão. 


# Exercício 2: Média de Vendas do Trimestre
# Cenário de Vendas: Seu gestor pediu a média do valor das suas últimas 3 vendas para a reunião trimestral.


# O que fazer: Faça um programa que receba o valor de três vendas, calcule e mostre a média aritmética entre elas. 

# Exercício 3: Alerta de Grande Negócio
# Cenário de Vendas: Na sua empresa, qualquer venda acima de R$ 50.000,00 precisa de uma aprovação extra do seu gestor. Você quer criar um alerta para não se esquecer.

# O que fazer: Crie um programa que recebe o valor de uma venda e, se o valor for maior que 50.000, exibe a mensagem "ALERTA: Negócio precisa de aprovação do gestor!". (Baseado no exercício da multa de velocidade ).


# Exercício 4: Política de Descontos Automática
# Cenário de Vendas: Sua empresa tem uma política de preços inteligente. Para produtos cujo custo de aquisição é menor que R$ 200,00, a margem de lucro é de 45%. Para custos iguais ou maiores que R$ 200,00, a margem é de 30%, pois são itens de maior giro.

# O que fazer: Crie um programa que receba o custo de um produto e calcule o preço final de venda com base nessa regra. (Inspirado no exemplo do comerciante ).