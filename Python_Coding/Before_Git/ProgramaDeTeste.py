# Esse é um programa de teste para praticar.

import sys

list_base = []

# Blablabla

resposta = input(f"Este é um programa de teste desenvolvido para fins pedagógicos, contanto, vamos lá.\n Você está interessando em continuar?\n Sim ou Não?\n")

if resposta in ["Sim","sim","s","S","Si","si"]:
    print("Ótimo! Vamos continuar.")
    idade = int(input(f"Qual sua idade?\n"))
    if idade <= 13:
        conf = input("Tem certeza?\n")
        if conf in ["Sim","sim","s","S","Si","si"]:
            sys.exit(f"\nFalhou")
    else:
        print(f"Certo, vamos continuar então.\nCaso não souber do que se trata esse programa, ele é uma série de perguntas nas quais vão te guiar para uma mensagem.\nBoa sorte!")
        



# Caso Negar
if resposta in ["Não","não","Nao","nao","N","n"]:
    print(f"Tudo bem, mas antes\n Responta: Carlos e Jośe")