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

# ---------

# Nível 1: A Decisão Binária (Sim ou Não)
# Aqui, a lógica é simples: SE uma condição for verdadeira, uma ação acontece. Se for falsa, nada acontece. Pense nisso como um alerta ou um lembrete no seu CRM.

# Exercício 1: Alerta de Cliente VIP
# Cenário de Vendas: Você quer identificar automaticamente clientes que fazem compras de alto valor para poder enviar um brinde especial e fortalecer o relacionamento. A regra é: qualquer compra acima de R$ 2.000,00 classifica o cliente como VIP.

# A Lógica (O "Se... Então..."): SE o valor da compra for maior que 2000, ENTÃO o sistema deve me alertar para enviar um brinde.

# Sua Tarefa: Crie um programa que pergunta o valor da compra. Se o valor for maior que 2000, ele deve exibir a mensagem: ALERTA: Cliente VIP! Preparar envio de brinde especial.
valorcompra= float(input("gostaria de saber o valor da compra"))
print(valorcompra)
if(valorcompra > 2000):
      print ("é cliente vip")
# Dicas de Código:

# Use float(input(...)) para capturar o valor da compra, pois pode ter centavos.

# A condição a ser verificada é valor_compra > 2000.

# Use uma única estrutura 

# if. 

# -----------

# Nível 2: A Escolha de Caminhos (Isso ou Aquilo)
# Agora, temos dois resultados possíveis para cada decisão. SE a condição for verdadeira, siga o caminho A. 
# SENÃO, siga o caminho B. É a clássica segmentação de leads.
valorcontrato=float(input("qual é o valor do contrato"))
if(valorcontrato > 10000):
      print("o vendedor é senior")
else:
      print("o vendedor é junior")
# Exercício 2: Direcionamento de Lead
# Cenário de Vendas: Na sua empresa, leads de grande potencial (valor de contrato acima de R$ 10.000,00) 
# são tratados por vendedores seniores. Os demais são tratados por vendedores juniores 
# para qualificação inicial.

# A Lógica (O "Se... Então..."): SE o valor potencial do lead for maior que 10.000, 
# ENTÃO encaminhe para a equipe Sênior. SENÃO, encaminhe para a equipe Júnior.

# Sua Tarefa: Crie um programa que pergunta o valor potencial de um novo lead. 
# Com base no valor, ele deve exibir Direcionar para: Equipe Sênior ou Direcionar para: Equipe Júnior.

# Dicas de Código:

# Você precisará de uma estrutura 

# if-else. 


# O if verifica a condição (valor_lead > 10000).

# O else captura todos os outros casos (menor ou igual a 10.000).

# --------------

# Nível 3: Múltiplas Alternativas (Classificação por Níveis)
# Aqui, a lógica se expande. Não temos apenas dois caminhos, mas vários. É como classificar seus clientes em categorias A, B ou C.

# Exercício 3: Sistema de Prioridade de Contato
# Cenário de Vendas: Você quer criar um sistema para priorizar seus contatos do dia. A regra é baseada no "lead score", uma pontuação que o marketing atribui a cada lead.

# Score acima de 80: Prioridade ALTA. Ligar imediatamente.

# Score entre 51 e 80: Prioridade MÉDIA. Enviar email hoje.

# Score de 50 ou menos: Prioridade BAIXA. Adicionar ao fluxo de nutrição.

# A Lógica (O "Se... Então..."):

# SE o score for > 80, ENTÃO a prioridade é ALTA.

# SENÃO, SE o score for > 50, ENTÃO a prioridade é MÉDIA.

# SENÃO, a prioridade é BAIXA.

# Sua Tarefa: Crie um programa que pergunta o "lead score" (um número de 0 a 100). O programa deve exibir a prioridade e a ação recomendada.
contatosdodia=float(input("gostaria de saber o leed score de cada programa"))
if(contatosdodia > 80):
      print ("se score for acima de 80 a prioridade é alta ligar imediatamente")
elif(contatosdodia > 51):
      print ("se o score for  de 51 a 80 a prioridade é media enviar email hoje")
else:
      print ("se o score for de 50 ou menos prioridade baixa acionar o fluxo de nutrição")



# Dicas de Código:

# Esta é a situação perfeita para usar a estrutura 

# if-elif-else. 



# A ordem das verificações é importante! Comece da maior para a menor. Se você checa se 

# score > 80 e dá falso, você já sabe que o número é 80 ou menos, então no elif só precisa checar se é > 50.

