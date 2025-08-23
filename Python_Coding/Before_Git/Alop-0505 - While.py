# >>> Atividade 1 - Metade dos números
Conta1 = 0
while Conta1 <= 9:
    numa1 = int(input("Informe um número inteiro: "))
    print(numa1/2)
    Conta1 += 1
    print(Conta1)

# >>> Atividade 2 - Algoritmo Média
Conta2 = 0
Roblox = 0
while Conta2 <= 9:
    numa2 = int(input(f"Informe um número:\n"))
    Roblox = numa2 + Roblox
    Conta2 += 1
print(f"A média dos números são de: {Roblox/10}")
# Só para saber se a soma está correta:
# print(f"Caso desejar saber, a soma dos números foi de: {Roblox}")

# >>> Atividade 3
##OI? COMO FAZ ISSO 😭

# >>> Atividade 4
par = 0
impar = 0
contador = 0
while contador <= 49:
    numer = int(input(f"Insira um número: "))
    if numer % 2 == 0:
        par += 1
    else:
        impar += 1
    contador += 1
print(f"A quantidade de números pares são de {par}, já de impares são de {impar} ")

# >>> Atividade 5 - Nomes & Letras
nomesroblox = 0
while nomesroblox <= 7:
    nome = input("Diga um nome!\n")
    letras = len(nome)
    print(f"O nome {nome} tem {letras} letras!")
    nomesroblox += 1

# >>> Atividade 6 - Nomes & Caracteres
nomes = []
contadorzinho = 0
while contadorzinho <= 11:
    nome = input(f"Diga um nome: ")
    nomes.append(nome)
    contadorzinho += 1
for nome in nomes:
    if nome:
        print(f"{nome}: {nome[0]}")
    else:
        print("Sem nome.")

# >>> Atividade 7 - Nome invertido & maiúscula
nome = input("Digite um nome: ")
nome_invertido = nome[::-1].upper()
print(f"Nome ao contrário e em maiúsculas: {nome_invertido}")

# >>> Atividade 8 - Maior que 30
numeros = 0
maior = 0
contadorazin = 0
while contadorazin <= 14:
    numbe = int(input(f"Diga um número\n"))
    if numbe >= 30:
        maior =+ maior + 1
        numeros =+ numeros + 1
    else:
        numeros =+ numeros + 1
    contadorazin += 1
print(f"O total de números foram de {numeros}, já o total de números maiores que 30 foram de {maior}.")