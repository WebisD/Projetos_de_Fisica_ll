from scipy.constants import c
import numpy as np

def EletricoToMagnetico(campo):

    cMag = campo/c

    return "--> Campo Magnético Máximo: "+ np.format_float_scientific(np.float32(cMag), precision=3) + " T"

def MagneticoToEletrico(campo):

    cEle = campo*c

    return "--> Campo Elétrico Máximo: "+ np.format_float_scientific(np.float32(cEle), precision=3) + " T"