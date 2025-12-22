## ATIVIDADE DO JAVA, MAS CONVERTIDA PARA PYTHON!
# cadastra números inseridos pelo usuário
# e verifica qual é o maior número.

numeros = [] # Lista criada
trava = 0 # trava da estrutura de repetição
indicador = 1 # Visual para o input

# Estrutura de repetição para receber números
while trava < 1:
    numero = int(input("\nDigite \"0\" para encerrar o programa.\nInforme o {}".format(indicador) + "º número: ")) # Recebe o número

    # Verifica se é igual a zero.
    if numero == 0:
        trava+=1 # Trava o código se Verdadeiro

    # Verifica se é um valor negativo
    elif numero < 0:
        print("\nPor favor, insira um valor positivo!") # Ignora a entrada e pede um novo número

    # Se for um número inteiro, e positivo, é adicionado a lista
    else:
        numeros.append(numero) # Adiciona o valor a lista
        indicador+=1 # Muda o indicador

print("O maior número foi:", max(numeros))