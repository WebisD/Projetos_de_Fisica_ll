import compToFreq
import freqToComp
import EmToBm
import BmToEm
import FreqToFreqAngAndK
import compToFreqAngAndK
import mathFunctions

def menu():
    print("╔════════════════════════════════════════════════════════╗")
    print("║ Calcular:                                              ║")
    print("║    1 - Frequência a partir do Comprimento de Onda      ║")
    print("║    2 - Comprimento de Onda a partir da Frequência      ║")
    print("║    3 - Campo Magnético a partir do Campo Elétrico      ║")
    print("║    4 - Campo Elétrico a partir do Campo Magnético      ║")
    print("║      - Número de onda e Frequência angular             ║")
    print("║        5 - A partir da Frequência                      ║")
    print("║        6 - A partir do Comprimento                     ║")
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
        elif opcao == 5:
            FreqToFreqAngAndK.calculaFreqAngAndK()
        elif opcao == 6:
            compToFreqAngAndK.calculaFreqAngAndK()

if __name__ == "__main__":
    main()