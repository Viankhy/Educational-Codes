while True:
    print("Menu - Atividades\n1. Atividade 11\n2. Atividade 20\n3. Atividade 23\n4. Atividade 57\n5. Sair")
    escolhaprinc = int(input("Escolha: "))

    if escolhaprinc == 5:
        print("Encerrando processo...")
        break

    elif escolhaprinc == 1:
    # atividade 20

        def somsub(x):
            if x <=10:
                return(x+5)
            elif x >=11:
                return(x-7)

        print("Valor somado - - -")
        valor = int(input(f"Informe um valor: "))
        print(somsub(valor))
        print()

    elif escolhaprinc == 2:
    # atividade 23

        def entre(x):
            if x >= 20 and x <=90:
                return(f'Esse número está entre 20 e 90.')
            else:
                return(f'Por favor, insira um número entre 20 e 90.')

        print("Número entre 20 e 90 - - -")
        valor2 = int(input(f"Por favor informe um número: "))
        print(entre(valor2))
        print()

    elif escolhaprinc == 3:
    # Atividade 57
    
        def divsob(x,y,z):
            if z == 1:
                return(f"A divisão do número {x} resulta em: {x/y:.2f}")
            elif z == 2:
                return(f"A sobra da divisão do número {x} é: {x%y:.2f}")

        def divsob2(x,y):
            return(f"A divisão resulta em: {x/y:.2f}, já a sobre é de {x%y:.2f}")

        print("Divisão e Sobra - - -")
        
        escolha = int(input(f"Por favor, selecione uma opção:\n1. Divisão\n2. Sobra\n3. Divisão & Sobra\n4. Sair\nEscolha: "))
        if escolha == 4:
            print("Saindo...")
            break
        if escolha not in [1,2,3]:
            print("Escolha invalida! Saindo...")
            break
        valor3 = float(input(f"Por favor, diga um número para ser dividido: "))
        valor4 = float(input(f"Por favor, diga um número para dividir: "))
        print()
        if valor4 == 0:
            print("O número Zero não pode dividir!")
            break
        if escolha in [1,2,3]:
            if escolha == 1:
                print(divsob(valor3,valor4,escolha))
                print()
            elif escolha == 2:
                print(divsob(valor3,valor4,escolha))
                print()
            elif escolha == 3:
                print(divsob2(valor3,valor4))
                print()
        else:
            print(f"Por favor, escolha um valor válido!")

    elif escolhaprinc == 4:
    # Atividade 11 - JESUS CRISTO ANA PAULA, EU TIVE QUE REESCREVER ESSE CÓDIGO UMAS 5 VEZES :cry:

        # ---- Funções
        def salario(x,y):
            # x = horas_trabalhadas
            # y = salario_minimo

            valor_bruto = y/3*x
            valor_total = 0
            if valor_bruto >= 0 and valor_bruto <= 3035:
                valor_total += valor_bruto
            elif valor_bruto >= 3036 and valor_bruto <= 3533:
                valor_total += valor_bruto * 7.5 / 100 - 182.16
            elif valor_bruto >= 3534 and valor_bruto <= 4688:
                valor_total += valor_bruto * 15 / 100 - 394.16
            elif valor_bruto >= 4689 and valor_bruto <= 5830:
                valor_total += valor_bruto * 22.5 / 100 - 675.49
            elif valor_bruto >= 5831:
                valor_total += valor_bruto * 27.5 / 100 - 908.73

            return("{:.2f}".format(valor_total))


        # ---- Código
        
        print("---- ---- ----")
        print(f"Bem-vindo(a) ao medidor de salário! Com esse programa, você será capaz de saber quanto vai receber com base na quantidade de horas trabalhadas.")
        sairagora = input("Caso desejar, pode encerrar o programa. ( Escreva 'Sim' para continuar, e 'Não' para encerrar o programa )\nResposta: ")
        if sairagora == "Sim":
            print("")
        elif sairagora == "Não":
            print("Encerrando...")
            break
        
        # ---- DIAS TRABALHADOS ( Parte de organização )
        dias_trabalhados = int(input(f"Quantos dias você trabalhou esse mês?\nResposta: "))
        if dias_trabalhados >= 32:
            print(f"Por favor, insira um valor válido!\n")
            break
        print()

        # ---- Horas trabalhadas
        horas_trabalhadas = int(input(f"Quantas horas você trabalhou durante esses {dias_trabalhados}? (Apenas números inteiros!)\nResposta: "))
        if horas_trabalhadas >= 720:
            print(f"Por favor, insira um valor válido! Um mês não tem mais de 720 horas.\n")
            break
        print()

        # ---- Valor do Salário Minímo
        salario_minimo = int(input(f"Qual o valor do salário minímo atualmente? (01/06/2025 = R$1550,00)\nResposta: "))
        print()

        print(f"Seu salário final é de: R${salario(horas_trabalhadas,salario_minimo)}")

    else:
        print("Opção invalida. Saindo...")
        break