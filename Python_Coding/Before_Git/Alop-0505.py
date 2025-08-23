# >>> Atividade 1 - Metade dos números
Conta1 = 0
for Conta1 in range(0,11):
    numa1 = int(input("Informe um número inteiro"))
    print(numa1/2)
    Conta1+1

# >>> Atividade 2 - Algoritmo Média
Conta2 = 0
Roblox = 0
for Conta2 in range(0,11):
    numa2 = int(input(f"Informe um número:\n"))
    Roblox = numa2 + Roblox
print(f"A média dos números são de: {Roblox/10}")
 # Só para saber se a soma está correta:
 # print(f"Caso desejar saber, a soma dos números foi de: {Roblox}")

# # >>> Atividade 3
### OI? COMO FAZ ISSO 😭

# >>> Atividade 4
par = 0
impar = 0
for i in range(50):
    numer = int(input(f"Insira um número: "))
    if numer % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"A quantidade de números pares são de {par}, já de impares são de {impar} ")

# >>> Atividade 5 - Nomes & Letras
for i in range(8):
    nome = input("Diga um nome!\n")
    letras = len(nome)
    print(f"O nome {nome} tem {letras} letras!")

# >>> Atividade 6 - Nomes & Caracteres
nomes = []

for i in range(12):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)
for nome in nomes:
    if nome:
        print(f"{nome}: {nome[0]}")
    else:
        print("Sem nome.")

# >>> Atividade 7 - Nome invertido & maiúscula
nome = input("Digite um nome: ")
nome_invertido = nome[::-1].upper()
print(f"Nome ao contrário e em maiúsculas: {nome_invertido}")

# # >>> Atividade 8 - Maior que 30
numeros = 0
maior = 0
for i in range(15):
    numbe = int(input(f"Diga um número\n"))
    if numbe >= 30:
        maior =+ maior + 1
        numeros =+ numeros + 1
    else:
        numeros =+ numeros + 1
print(f"O total de números foram de {numeros}, já o total de números maiores que 30 foram de {maior}.")