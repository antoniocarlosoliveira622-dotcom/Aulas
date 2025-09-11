# Três etapas, assim como um funil de vendas:

# Topo de Funil: O Conceito (O que é o seu Playbook de Vendas?)

# Meio de Funil: A Execução (Seguindo o Script Passo a Passo)

# Fundo de Funil: A Tomada de Decisão (Qualificação e Fechamento)

# 1. Topo de Funil: O Que é um Algoritmo e Como Estruturá-lo?
# No nosso mundo, não fazemos nada sem um plano, certo? Um algoritmo é exatamente isso: 

# um conjunto de regras e procedimentos lógicos que levam à solução de um problema em um número finito de passos.

# Entrada (Input): Um novo lead que caiu no seu CRM.

# Processo (Algoritmo): As etapas que você segue: qualificação, apresentação, negociação, etc.

# Saída (Output): O resultado: a venda fechada ou o lead perdido.

# Fluxograma (O Desenho no Quadro Branco): É a representação visual do seu funil de vendas, 
# usando símbolos gráficos para mostrar o fluxo do processo. 

# Pseudocódigo (O Rascunho em Tópicos): É como escrever o roteiro de vendas em um bloco de notas, 
# usando uma linguagem simples, sem se preocupar com a formatação exata. É o meio do caminho entre a ideia e o script final.

# Linguagem de Programação (O Script Final no CRM): É o script detalhado, com as palavras exatas e a sintaxe 
# correta que o computador (ou um novo vendedor) precisa seguir à risca. 

# Entrada de Dados (input): Você faz perguntas e guarda as respostas.

# No nosso mundo: "Qual o seu nome?" / "Qual o seu orçamento?"
# Para guardar o que o usuário digita, usamos a função input()
nome = input("Digite seu nome:")
#  Pede um valor e já converte para número com decimal
orcamento = float(input("Qual seu orçamento?"))

# Saída de Dados (print): Você apresenta informações ou confirma o que ouviu.

# No nosso mundo: "Ok, João, entendi que seu orçamento é de R$ 5.000."

# Em Python: Para mostrar algo na tela, usamos a função print().

# Mostra uma mensagem na tela combinando texto e o valor guardado
print(f'Ok, {nome}, seu orçamento é de R${orcamento}')

# As "Gavetas" de Informação (Variáveis e Tipos de Dados)
# Para guardar as informações do cliente, usamos 

# variáveis: um espaço na memória com um nome. Pense nos campos do seu CRM: 

# Nome do Cliente, Valor da Oportunidade, etc.

# Cada informação tem um tipo, assim como categorizamos nossos leads. Os tipos básicos são:

# Inteiro (int): Quantidade de licenças (ex: 10). Um número inteiro.



# Ponto Flutuante (float): Valor da proposta (ex: 15250.75). Um número com decimais.


# String (str): Nome do cliente (ex: 'Empresa X'). É um texto.


# Lógico (bool): É o decisor? (True / False). É um simples Sim ou Não.

# 3. Fundo de Funil: A Tomada de Decisão (Estrutura Condicional)
# estrutura de seleção ou condicional permite que o programa escolha um caminho diferente com base em uma condição

# expressões lógicas 
# True (Verdadeiro) ou False (Falso).

# Operadores Relacionais: São usados para comparar valores.

# == (Igual a): O cargo do contato é igual a "Diretor"? 

# > (Maior que): O orçamento é maior que R$ 20.000? 

# != (Diferente de): O status do lead é diferente de "Perdido"? 

# Operadores Lógicos: Usados para combinar comparações.

# and (E): O lead é qualificado se o orçamento é > 20k E o contato é o decisor.

# or (OU): Oferecer desconto se o pagamento for à vista OU se for final de trimestre.

# 1. Estrutura Condicional Simples (if)
velocidade = float(input("Informe a velocidade:"))
if(velocidade > 50):
    print('voce sera multado')

# 2. Estrutura Condicional Composta (if-else)
# No nosso mundo: "Um comerciante quer vender com 45% de lucro se o valor for menor que R$ 20.
#  SENÃO, o lucro será de 30%." 

valor = float(input("valor da compra:"))
if valor < 20.00:
    valorVenda = valor * 1.45 
else:
    valorVenda = valor * 1.30
    
print(f'Valor da venda: {valorVenda:.2f}') 