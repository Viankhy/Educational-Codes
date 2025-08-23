# Recuperação

### NECESSÁRIO COMENTAR AS LINHAS DE CÓDIGO CASO FOR TESTAR!!!

# 1. Faça um programa que receba o ano atual, e o de nascimento da pessoa. Com isso, calcule a idade da pessoa, e quanto ela terá em 2050.

### Ano atual, nascimento e idade.
anoatual = int(input("Informe o ano em que estamos atualmente: "))
anonascimento = int(input("Informe o ano de seu nascimento: "))

### verificar idade.
idade = anoatual - anonascimento

confirmacao = str(input(f"Sua idade atual é de {idade}, correto? (Apenas 'Sim' ou 'Não')\nResposta: "))

### Calculo e respostas de idade
### Se respondido Sim, o calculo será feito, e as respostas serão entregues.
if confirmacao == "Sim":
    print("Continuando")
    print(f"Sua idade atual é de {idade}\nSua idade em 2050 será de", 2050-anonascimento)
### Se respondido Não, será realizado uma alteração na idade, e as respostas serão entregues.
elif confirmacao == "Não":
    idade = int(input(f"Entendido, corrigindo...\nInsira sua idade atual: "))
    print(f"Sua idade atual é de {idade}\nSua idade em 2050 será de", 2050-anonascimento)

# 2. Colocar o código anterior em uma estrutura de repetição, tanto While quanto For i in range

### Em estrutura While ( Comentários removiso em pró de uma melhor organização )
x = 0
while x <= 4:
    anoawhiletual = int(input("Informe o ano em que estamos atualmente: "))
    anowhilenascimento = int(input("Informe o ano de seu nascimento: "))

    idadewhile = anoawhiletual - anowhilenascimento

    confirmacaow = str(input(f"Sua idade atual é de {idadewhile}, correto? (Apenas 'Sim' ou 'Não')\nResposta: "))

    if confirmacaow == "Sim":
        print("Continuando")
        print(f"Sua idade atual é de {idadewhile}\nSua idade em 2050 será de", 2050-anowhilenascimento)
    elif confirmacaow == "Não":
        idadewhile = int(input(f"Entendido, corrigindo...\nInsira sua idade atual: "))
        print(f"Sua idade atual é de {idadewhile}\nSua idade em 2050 será de", 2050-anowhilenascimento)
    
    x += 1

### Em estrutura For i in ( Comentários removiso em pró de uma melhor organização )
for i in range (0,5,1):
    anoafortual = int(input("Informe o ano em que estamos atualmente: "))
    anofornascimento = int(input("Informe o ano de seu nascimento: "))

    idadefor = anoafortual - anofornascimento

    confirmacaow = str(input(f"Sua idade atual é de {idadefor}, correto? (Apenas 'Sim' ou 'Não')\nResposta: "))

    if confirmacaow == "Sim":
        print("Continuando")
        print(f"Sua idade atual é de {idadefor}\nSua idade em 2050 será de", 2050-anofornascimento)
    elif confirmacaow == "Não":
        idadefor = int(input(f"Entendido, corrigindo...\nInsira sua idade atual: "))
        print(f"Sua idade atual é de {idadefor}\nSua idade em 2050 será de", 2050-anofornascimento)

# 3. Receba alturas e idades, se for acima de 50 calcule a média de altura.

pessoas = 0
alturas = 0
while True:
    altura = int(input("Por favor, insira sua altura em CM: "))
    idadealt = int(input("Insira sua idade: "))
    if idadealt >= 50:
        print("Registrado...")
        alturas += altura
        pessoas += 1
        print(alturas)
    elif idadealt >= 1 and idadealt <= 49:
        print("Resgistrado... (Não registrado.)")
    elif idadealt <= 0:
        print("Encerrando programa...")
        break
print("A média de altura de pessoas com 50 anos para cima é de:", alturas/pessoas)
