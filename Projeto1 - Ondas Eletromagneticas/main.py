import compToFreq
import freqToComp

def menu():
    print("╔════════════════════════════════════════════════════════╗")
    print("║ Calcular:                                              ║")
    print("║    1 - Frequência a partir do Comprimento de Onda      ║")
    print("║    2 - Comprimento de Onda a partir da Frequência      ║")
    print("║                                                        ║")
    print("║ 0 - Sair                                               ║")
    print("╚════════════════════════════════════════════════════════╝")
    return

def main():

    while True:
        menu()
        opcao = int(input("Digite uma opção: "))

        if(opcao not in (1,2,0)):
            continue

        if(opcao == 0):
            return
        elif opcao == 1:
            compToFreq.pedeComprimento()
        elif opcao == 2:
            freqToComp.pedeFrequencia()



if __name__ == "__main__":
    main()