import interface

'''
Obs: Todas as entrads (e saídas) são em W/m^2

    Opcão com um polarizador:
    
        Entra com:
            1) I0
                I0 = I0
                I = halfLaw(I0)
            2) I
                I0 = reverseHalfLaw(I)
                I = I
                
    Opção com 2 polarizadores:
        
        Entra com:
            1) I0
                I0 = I0
                I1 = halfLaw(I0)
                I2 = malusLaw(I1, angulo)
            2) I1
                I0 = reverseHalfLaw(I1)
                I1 = I1
                I2 = malusLaw(I1, angulo)
            3) I2
                I0 = reverseHalfLaw(I1)
                I1 = reverseMalusLaw(I2, angulo)
                I2 = I2
                
    Opcão com 3 polarizadores:
        Aí o negocio complica um pouco :P                         
'''
def main():
    interface.inicializa()

if __name__ == "__main__":
    main()