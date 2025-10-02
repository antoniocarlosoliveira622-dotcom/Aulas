# Exercício 1: Calculando o Preço Base (O Começo de Tudo)

# Cenário de Vendas: Você está montando uma proposta. O primeiro passo é calcular o valor subtotal, 
# que é o preço de um item multiplicado pela quantidade que o cliente quer comprar.

# O Roteiro em Português (O que o estagiário deve fazer):
#     1.  Pergunte: "Qual o preço unitário do produto?" e anote.
#     2.  Pergunte: "Qual a quantidade de itens?" e anote.
#     3.  Calcule o subtotal fazendo: `valor anotado do preço` x `valor anotado da quantidade`.
#     4.  Mostre o resultado final dizendo: "O subtotal do pedido é: R$ [resultado]".
# Sua Tarefa: Traduza o roteiro acima para um código Python.

# ----------------------------------------------------------

### Exercício 2: Adicionando um Desconto por Volume (Lógica Simples `if`)

# Agora vamos adicionar a primeira regra de negócio.

# Cenário de Vendas: A empresa oferece um desconto de 10% para incentivar compras maiores. 
# A regra é: se o cliente comprar mais de 10 itens, ele ganha o desconto.

# O Roteiro em Português:
#     1.  Faça exatamente como no exercício 1 para calcular o `subtotal`.
#     2.  Comece com uma anotação de que o `desconto` é `0`.
#     3.  **SE** a `quantidade` que o cliente comprou for **maior que 10**:
#           * Recalcule o `desconto` para ser `subtotal * 0.10` (que é 10%).
#     4.  Calcule o `total_final` fazendo: `subtotal - desconto`.
#     5.  Mostre o subtotal, o valor do desconto e o total final.
#  Sua Tarefa: Crie um programa que calcula o subtotal e aplica um desconto de 10% apenas se a quantidade for maior que 10.

# ----------------------------------------------------------

### Exercício 3: Adicionando a Taxa de Urgência (Lógica `if-else`)

# Vamos adicionar outra regra. Desta vez, com dois caminhos possíveis.

# Cenário de Vendas: O frete padrão custa R$ 20,00. Porém, se o cliente pedir entrega urgente, o custo do frete sobe para R$ 100,00.
# O Roteiro em Português:
#     1.  Pergunte: "A entrega é urgente? (s/n)" e anote a resposta.
#     2.  SE a resposta for exatamente igual a "s":
#           Anote que a `taxa_frete` é `100.00`.
#     3.  SENÃO (para qualquer outra resposta):
#           Anote que a `taxa_frete` é `20.00`.
#     4.  Mostre na tela o valor do frete escolhido.
# Sua Tarefa: Crie um programa que define o valor do frete com base na urgência da entrega.


# ----------------------------------------------------------


### Exercício 4: A Calculadora de Proposta Completa (Juntando Tudo)

# Cenário de Vendas: Juntar os cálculos de preço base, desconto por volume e taxa de frete para gerar o valor final de uma proposta comercial.
# O Roteiro em Português:
#     1.  Peça o `preço unitário` e a `quantidade`.
#     2.  Peça se a `entrega é urgente`.
#     3.  Calcule o `subtotal`.
#     4.  Defina o `desconto` (usando a regra do "maior que 10 itens").
#     5.  Defina a `taxa_frete` (usando a regra da "entrega urgente").
#     6.  Calcule o `total_final` fazendo: `subtotal - desconto + taxa_frete`.
#     7.  Mostre um resumo completo da proposta.
# Sua Tarefa: Crie o programa final que faz tudo isso. Apenas junte as peças dos exercícios anteriores.
