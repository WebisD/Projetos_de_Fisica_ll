from scipy.constants import c, pi
import numpy as np

def numeroDaOnda(opcao, entrada):
    if opcao == 1:                  # entrada = frequencia
        nOnda = (2*pi*entrada)/c
    elif opcao == 2:                # entrada = comprimento de onda
        nOnda = (2*pi)/entrada

    print("--> Numero da Onda: "+ np.format_float_scientific(np.float32(nOnda), precision=3) + " rad/m")

    return

def freqAngular(opcao, entrada):
    if opcao == 1:                # entrada = frequencia
        w = 2*pi*entrada
    elif opcao == 2:              # entrada = comprimento de onda
        w = (2*pi*c)/entrada

    print("--> Frequência Angular: " + np.format_float_scientific(np.float32(w), precision=3) + " rad/s")

    return

def analisaUnidade(unidade):
    valor = 1

    if unidade == "nm":
        valor = 10**-9
    elif unidade == "mm":
        valor = 10**-6
    elif unidade == "m":
        valor = 1
    elif unidade == "km":
        valor = 10**3
    else:
        print("Ta errado :(")
        tipoEscolhido(2)
    return valor

def tipoEscolhido(opcaoEntr):

    if opcaoEntr == 1:
        escolha = input("\nDigite a frequência (Ex. 700 Hz): ")
    elif opcaoEntr == 2:
        escolha = input("\nDigite o comprimento de onda (Ex. 700 km): ")

    valor, unidade = escolha.split(" ")
    valor = float(valor)

    if opcaoEntr == 2:
        expo = analisaUnidade(unidade)
        valor *= expo

    return valor

def freqAngToComp(freqAngularValue):
    comp = (2*pi*c)/freqAngularValue
    return comp

def numeroOndaToComp(numOndaValue):
    comp = (2*pi)/numOndaValue
    return comp

def menu():
    print("\nEntrar com:")
    print("\t1 - Frequência")
    print("\t2 - Comprimento de Onda")

    return

def pedeValor(opcaoCarac):

    while True:
        menu()
        opcaoEntr = int(input("Digite uma opção: "))

        if (opcaoEntr not in (1, 2)):
            continue

        tipo = tipoEscolhido(opcaoEntr)

        if opcaoCarac == 1:
            numeroDaOnda(opcaoEntr, tipo)
            break
        elif opcaoCarac == 2:
            freqAngular(opcaoEntr, tipo)
            break
