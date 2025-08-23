# Prova ( Confirmando se fiz certo )
# valor = 350
# desconto = (350 * 8)/100
# print(f"Aline gastou R${valor - desconto}, no presente de sua mãe")

# Atividade Ana Paula ( Aula )
nume1 = float(input("Qual sua primeira nota"))
nume2 = float(input("Qual sua segunda nota"))
nume3 = float(input("Qual sua terceira nota\n"))

if (nume1>=0 and nume1<=10) and (nume2>=0 and nume2<=10) and (nume3>=0 and nume3<=10):
    peso1 = float(input("Diga o primeiro peso"))
    peso2 = float(input("Diga o segundo peso"))
    peso3 = float(input("Diga o terceiro peso"))
    if (peso1>=1 and peso1<=10) and (peso2>=0 and peso2<=10) and (peso3>=0 and peso3<=10):    
        print((nume1*peso1 + nume2*peso2 + nume3*peso3)/peso1+peso2+peso3)
else:
    print("É necessário que o número seja entre 0 a 10 ( ou 1 a 10 )")