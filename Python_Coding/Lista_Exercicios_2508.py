# # Exercicio 6.1 - Modifique o programa da listagem 6.2 para ler 7 notas em vez de 5.
# while True:
#     notas = [0,0,0,0,0,0,0]   #1
#     nomes=['','','','','','','']
#     soma = 0
#     x = 0
#     while x < 7:
#       nomes[x] = input('Informe seu nome: ')
#       notas[x] = float(input(f'Nota {x}:')) #2
#       soma += notas[x]
#       x += 1
#     x = 0                 #3
#     while x < 7:          #4
#       print(f'Nota {x}: {notas[x]:6.2f}')
#       x += 1
#     print(f'Média: {soma / x:5.2f}')

### Lista de Exercícios 3 [vale-nota]: 3BIM (PARTE I)

# 1. Crie uma lista
# 2. O nome da sua lista deve ser a primeira letra inicial do seu nome com a primeira letra inicial do seu segundo nome.
#    Exemplo: Ana Paula, nome da lista AP.
# 3. Logo em seguida "popule" a lista, ou seja, insira 5 valores da seguinte maneira:
#    a) o primeiro elemento: é o dia do seu nascimento;
#    b) o segundo elemento: o mês do seu nascimento;
#    c) o terceiro elemento: o ano do seu nascimento;
#    d) o quarto elemento: a data de hoje (XX/XX);
#    e) e o quinto elemento é o ano em que estamos.
# Observação: inserir utilizando o exemplo de Adição de dados por concatenação de dados e depois utilizar a função append]

y = 0

print("Por favor, insira os dados pedidos;")
VS = []
while y <= 0:
    DiaNascimento = int(input("Insira o Dia do seu Nascimento: "))
    VS.append(DiaNascimento)
    MesNascimento = int(input("Insira o Mês do seu Nascimento: "))
    VS.append(MesNascimento)
    AnoNascimento = int(input("Insira o Ano do seu Nascimento: "))
    VS.append(AnoNascimento)

    # Datas Atuais ( Organizadas mais a frente da lista )
    input("Insira a data de hoje, (dia): ")
    Mes01 = int(input("Insira a data de hoje, (mês): "))
    if Mes01 == 1:
        Mes01 = "Janeiro"
    elif Mes01 == 2:
        Mes01 = "Fevereiro"
    elif Mes01 == 3:
        Mes01 = "Março"
    elif Mes01 == 4:
        Mes01 = "Abril"
    elif Mes01 == 5:
        Mes01 = "Maio"
    elif Mes01 == 6:
        Mes01 = "Junho"
    elif Mes01 == 7:
        Mes01 = "Julho"
    elif Mes01 == 8:
        Mes01 = "Agosto"
    elif Mes01 == 9:
        Mes01 = "Setembro"
    elif Mes01 == 10:
        Mes01 = "Outubro"
    elif Mes01 == 11:
        Mes01 = "Novembro"
    elif Mes01 == 12:
        Mes01 = "Dezembro"
    VS.append(Mes01)

    AnoAtual = int(input("Insira o Ano que estamos: "))
    VS.append(AnoAtual)
    print() # Quebra de linha   
    y += 1

# Logo após, faça as seguintes manipulações com os índices da lista:
# 
# 1. exiba toda a lista.
# 2. exiba somente o terceiro elemento.
# 3. exiba todos os elementos menos o último.
# 4. exiba o terceiro e quarto elementos.
# 5. substitua a data de hoje pelo nome do mês atual.
# 6. exiba o quarto elemento.
# 7. exiba somente os elementos dos índices pares.
# 8. exiba somente os elementos dos índices ímpares.
# 9. some 1 (hum) para cada elemento numérico, menos para o quarto 🤪

print(f"Lista completa (Teste): {VS[0:5]}") # 1
print("Lista, somente o terceiro elemento:", VS[2]) # 2
print(f"Lista, sem o ultimo valor: {VS[0:4]}") # 3
print("Lista, apenas terceiro e quarto elemento:", VS[2:4]) # 4
print(f"Lista, quarto elemento: {VS[3]}") # 6
pares = [x for x in VS if isinstance(x, int) and x % 2 == 0] # 7
print("Lista, somente pares:", pares) # 7
impares = [x for x in VS if isinstance(x, int) and x % 2 == 1] # 8
print("Lista, somente impares:", impares) # 8
soma1 = [x + 1 if isinstance(x, int) else x for x in VS] # 9
print("Lista, com a soma de +1:", soma1) # 9
print("\nLista 2.0\n")

# Exemplo:
# AP = [31, 08, 76, agosto, 2025]
# Resultado do acréscimo de 1: AP = [32, 09, 77, agosto, 2026]
# 10. faça uma cópia da lista. O nome dela é a inicial do seu segundo nome com a inicial do primeiro nome. Exemplo: AP agora também é PA.
# 11. modifique o índice 0 inserindo o nome do seu pet. Se não tiver pet, invente um nome para o seu pet imaginário.
# 12. exiba a cópia da lista
# A partir da cópia:
# 13. insira como sexto elemento da lista uma lista com o primeiro nome dos seus responsáveis ou de duas pessoas muito próximas.
# 14. exiba somente o primeiro nome da lista do sexto elemento.
# 15. crie uma lista nova a partir da lista cópia (no meu caso PA) e insira o sétimo elemento que será o seu prontuário. O nome desta lista é seuProntuárioE_AsIniciaisDoSeuNome. No meu caso: AP122875.
# 16. Complete a lista com números de 0 a 50.
# 
# Obs.: manter o que já há na lista e usar range com list
# 17. Delete os números pares dos números gerados de 0 a 50. Obs.: usar del

SV = [] # 10
Pet = str(input("Insira o nome do seu pet: "))
SV.append(Pet) # 11
SV.append(DiaNascimento) # 10
SV.append(MesNascimento) # 10
SV.append(AnoNascimento) # 10
SV.append(Mes01) # 10
SV.append(AnoAtual) # 10
print(f"Lista {SV}, (Cópia da lista anterior)") # 12

Responsaveis = [] # 13
resp1 = str(input("Por favor, diga o nome do seu 1º resposável: ")) # 13
Responsaveis.append(resp1) # 13
resp2 = str(input("Por favor, diga o nome do seu 2º resposável: ")) # 13
Responsaveis.append(resp2) # 13
amigo1 = str(input("Por favor, diga o nome do seu 1º amigo: ")) # 13
Responsaveis.append(amigo1) # 13
amigo2 = str(input("Por favor, diga o nome do seu 2º amigo: ")) # 13
Responsaveis.append(amigo2) # 13
print(f"Lista dos responsáveis & amigos (6º Elemento): {Responsaveis}") # 14

SV2 = [] + SV + Responsaveis # 15
Prontuario = str(input(f"Insira seu prontuário: ")) # 15
SV2.append(Prontuario) # 15

NumExt = [] # 16
NumExt.extend(range(51)) # 16
for i in range(len(NumExt)-1, -1, -1): # 17
    if isinstance(NumExt[i], int) and NumExt[i] % 2 == 0: # 17
        del NumExt[i] # 17

print(f"Lista completa após a execução de todos os passos pedidos ao decorrer da atividade: {SV2 + NumExt}")
print("Fim da lista 3ºBim, iniciando exercicios 6.X...")
print()

### Lista de Exercícios 3 [vale-nota]: 3BIM (PARTE I)

### Exercício 6.2
# Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
# Exemplo: Lista 1: AP = [31,8,1976,'21/08',2025]
# Lista 2: PA = ['dia','mês','ano','ana','anoAtual']
# Lista 3: APcomPA = [31,8,1976,'21/08',2025,'dia','mês','ano','ana','anoAtual']

print(f"Exercicio 6.2\nUma lista que junta as listas VS e SV da atividade 'Lista 3ºBim'.\n{VS + SV[1:]}\n")


### Exercício 6.3
# Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos. Dica: usar um if para comparar os elementos

lista1 = VS
lista2 = SV[1:]

ListaNoRepet = []
for item in lista1:
    if item not in ListaNoRepet:
        ListaNoRepet.append(item)
for item in lista2:
    if item not in ListaNoRepet:
        ListaNoRepet.append(item)

print(f"Exercicio 6.3\nLista sem conteúdo repetido: {ListaNoRepet}\n")

### Exercício 6.4
# A partir do programa 6.2, o qual gerou um terceira lista. Remove os elementos de índices pares da lista gerada.

ListaRepet = [x for x in ListaNoRepet if isinstance(x, int) and x % 2 == 1] # 8 ( Copiado da atividade )
print(f"Exercicio 6.4\nLista sem a presença de números 'Pares': {ListaRepet}") # 8 ( Copiado da atividade )