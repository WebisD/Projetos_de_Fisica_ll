import compToFreq
import freqToComp
import campos
import caracOndas

def menu():
    print()
    print("╔════════════════════════════════════════════════════════╗")
    print("║ Calcular:                                              ║")
    print("║    1 - Frequência a partir do Comprimento de Onda      ║")
    print("║    2 - Comprimento de Onda a partir da Frequência      ║")
    print("║    3 - Campo Elétrico a partir do Campo Magnético      ║")
    print("║    4 - Campo Magnético a partir do Campo Elétrico      ║")
    print("║    5 - Número de Onda                                  ║")
    print("║    6 - Frequência Angular                              ║")
    print("║ 0 - Sair                                               ║")
    print("╚════════════════════════════════════════════════════════╝")
    return

def main():

    while True:
        menu()
        opcao = int(input("Digite uma opção: "))

        if(opcao not in (1,2, 3, 4, 5, 6,0)):
            continue

        if(opcao == 0):
            return
        elif opcao == 1:
            compToFreq.pedeComprimento()
        elif opcao == 2:
            freqToComp.pedeFrequencia()
        elif opcao == 3:
            campos.pedeValor(1)
        elif opcao == 4:
            campos.pedeValor(2)
        elif opcao == 5:
            caracOndas.pedeValor(1)
        elif opcao == 6:
            caracOndas.pedeValor(2)



if __name__ == "__main__":
    main()