# Nível 1 (Revisão): A Decisão Simples (Sim ou Não)
# Lembrete: if. SE algo for verdade, uma ação acontece. Senão, nada de especial ocorre.

# Exercício: Alerta de Contrato Vencendo

# Cenário de Vendas: Para garantir a renovação, você precisa ser alertado quando um contrato de cliente está prestes a vencer. 
# A regra é: se faltam 30 dias ou menos, o sistema deve te avisar.

# A Lógica (O "Se... Então..."): SE o número de dias para o contrato vencer for MENOR QUE 31, ENTÃO o sistema deve exibir um alerta.

# Sua Tarefa: Crie um programa que pergunta "Quantos dias faltam para o contrato vencer?". Se o número for 30 ou menos, 
# ele deve exibir a mensagem: ALERTA DE RENOVAÇÃO: Entrar em contato com este cliente para negociar a renovação!

# Pergunta e anota o número de dias. Usamos int() pois "dias" é um número inteiro.
dias_para_vencer_string = input("Quantos dias faltam para o contrato vencer?")
dias_para_vencer = int(dias_para_vencer_string)

# if, elif, else
if(dias_para_vencer <= 30):
    print("ALERTA DE RENOVAÇÃO: Entrar em contato com este cliente para negociar a renovação!")


# Nível 2 (Revisão): A Escolha de Caminhos (Isso ou Aquilo)
# Lembrete: if-else. SE algo for verdade, faça A. SENÃO, faça B.

# Exercício: Script de Abordagem (Novo Cliente vs. Cliente Antigo)

# Cenário de Vendas: Sua abordagem inicial muda se você está falando com um lead que nunca comprou ou com um cliente que já está na base.
# Você precisa de um sistema que te dê o script certo.

# A Lógica (O "Se... Então..."): SE a resposta para "É a primeira compra do cliente?" for "sim", ENTÃO mostre o script de boas-vindas. 
# SENÃO, mostre o script de cliente recorrente.

# Sua Tarefa: Crie um programa que pergunta: É a primeira compra deste cliente? (s/n). Se o usuário digitar s, 
# o programa exibe Script: "Bem-vindo! Que bom ter você começando com a gente.". Se digitar qualquer outra coisa, 
# exibe Script: "Que bom te ver de volta! Obrigado pela confiança contínua.".




# Nível 3 (Revisão): Múltiplas Alternativas (Classificação por Níveis)
# Lembrete: if-elif-else. SE a condição A for verdade, faça X. SENÃO, SE a condição B for verdade, faça Y. SENÃO, faça Z.

# Exercício: Cálculo de Bônus por Performance

# Cenário de Vendas: O bônus semestral é pago de acordo com a porcentagem da meta atingida.

# Acima de 120%: Bônus Ouro

# Entre 100% e 120% (inclusive): Bônus Prata

# Abaixo de 100%: Sem bônus de performance.

# A Lógica (O "Se... Então..."):

# SE a porcentagem da meta for > 120, ENTÃO o bônus é Ouro.

# SENÃO, SE a porcentagem da meta for >= 100, ENTÃO o bônus é Prata.

# SENÃO, não há bônus.

# Sua Tarefa: Crie um programa que pergunta qual porcentagem da meta foi atingida. Ele deve exibir qual o nível de bônus o vendedor receberá.