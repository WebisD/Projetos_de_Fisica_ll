import compToFreq
import freqToComp
import EmToBm
import BmToEm
import mathFunctions

def menu():
    print("╔════════════════════════════════════════════════════════╗")
    print("║ Calcular:                                              ║")
    print("║    1 - Frequência a partir do Comprimento de Onda      ║")
    print("║    2 - Comprimento de Onda a partir da Frequência      ║")
    print("║    3 - Campo Magnético a partir do Campo Elétrico      ║")
    print("║    4 - Campo Elétrico a partir do Campo Magnético      ║")
    print("║                                                        ║")
    print("║ 0 - Sair                                               ║")
    print("╚════════════════════════════════════════════════════════╝")
    return

def main():

    while True:
        menu()
        opcao = int(input("Digite uma opção: "))

        if(opcao not in (1,4,0)):
            continue

        if(opcao == 0):
            return
        elif opcao == 1:
            compToFreq.pedeComprimento()
        elif opcao == 2:
            freqToComp.pedeFrequencia()
        elif opcao == 3:
            EmToBm.calculaBm()
        elif opcao == 4:
            BmToEm.calculaEm()

if __name__ == "__main__":
    main()