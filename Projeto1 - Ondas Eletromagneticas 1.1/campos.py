from scipy.constants import c
import numpy as np

def EletricoToMagnetico(campo):
    cEle = float(campo[0:-4])

    cMag = cEle/c

    print("--> Campo Magnético Máximo:"+ np.format_float_scientific(np.float32(cMag), precision=3) +" T")

def MagneticoToEletrico(campo):
    cMag = float(campo[0:-2])

    cEle = cMag*c

    print("--> Campo Elétrico Máximo:"+ np.format_float_scientific(np.float32(cEle), precision=3) +" T")


def pedeValor(opcao):

    if opcao == 1:
        campo = input("\nDigite o valor do Campo Magnético Máximo (Ex. 500 T): ")
        MagneticoToEletrico(campo)
    elif opcao == 2:
        campo = input("\nDigite o valor do Campo Elétrico Máximo (Ex. 500 V/m): ")
        EletricoToMagnetico(campo)