import energiaCinetica as eC
import energiaPotencial as eP
import energiaTotal as eT
import raioOrbita as rO
import ComprimentoOndaTransição as cPT
import ComprimentoOndaTransicaoSerie as cPTS
import energiaFoton as eF

def getInputEnergy(n):
    try:
        value = float(n.replace(',','.'))
    except ValueError:
        return ["Erro", "Não foi possível interpretar o valor digitado como um número."]

    number = round(value)

    if (abs(value - number) <= 0.10000000000000009):
        E_Cinetica = eC.calcEnergiaCinetica(number)
        E_Potencial = eP.calcEnergiaPotencial(number)
        E_Total = eT.calcEnergiaTotal(number)
        R_Orbita = rO.calcRaio(number)
        Resposta = '''Energia Cinética: {} eV
        
Energia Potencial: {} eV

Energia Total: {} eV

Raio da Órbita: {} nm
        '''
        return ["Resultado", Resposta.format(E_Cinetica, E_Potencial, E_Total, R_Orbita)]
    else:
        return ["Erro", "Digite um valor inteiro."]


def tryFloat(n):
    try:
        value = float(n.replace(',','.'))
        return True
    except ValueError:
        return False

def tryInt(value, number):
    if (abs(value - number) <= 0.10000000000000009):
        return True
    else:
        return False

def getInputComp(ni, nf):

    if not tryFloat(ni):
        return ["Erro", "Não foi possível interpretar o valor em NI como um número."]
    if not tryFloat(nf):
        return ["Erro", "Não foi possível interpretar o valor em NF como um número."]

    valueNi = float(ni.replace(',', '.'))
    valueNf = float(nf.replace(',', '.'))

    numberNi = round(valueNi)
    numberNf = round(valueNf)

    if not tryInt(valueNi, numberNi):
        return ["Erro", "Digite um valor inteiro em NI."]
    if not tryInt(valueNf, numberNf):
        return ["Erro", "Digite um valor inteiro em NF."]

    if numberNf > 0:
        comp = abs(cPT.calcularComprimentoTransacao(numberNi, numberNf))
        Resposta = "Comprimento de Onda emitido pelo átomo:\n\n                      λ = {0:.4e} nm"
    else:
        return ["Erro", "Digite um valor maior em NF."]

    return ["Resultado", Resposta.format(comp)]

def getInputSerie(ni, serie):
    if not tryFloat(ni):
        return ["Erro", "Não foi possível interpretar o valor em NI como um número."]

    valueNi = float(ni.replace(',', '.'))
    numberNi = round(valueNi)

    if not tryInt(valueNi, numberNi):
        return ["Erro", "Digite um valor inteiro em NI."]

    result = cPTS.calcComprimentoComSerie(numberNi, serie)

    if result[0] != "Erro":
        if result[1] == "":
            Resposta = "Comprimento de Onda emitido pelo átomo:\n\n                     λ = {0:.4e} nm" \
                       "\n\n\nEspectro do fóton emitido: {1}"
            return ["Resultado", Resposta.format(result[0], result[2])]
        else:
            Resposta = "Comprimento de Onda emitido pelo átomo:\n\n                      λ = {0:.4e} nm" \
                       "\n\n\nEspectro do fóton emitido: {1}\n\nCor do fóton emitido: {2}"
            return ["Resultado", Resposta.format(result[0], result[2], result[1])]
    else:
        return result

def getInputPhoton(comp, unidade):
    if not tryFloat(comp):
        return ["Erro", "Não foi possível interpretar o valor em λ como um número."]

    valueComp = float(comp.replace(',', '.'))

    result = eF.nFinal(valueComp, unidade)

    if result[0] != "Erro":
        Resposta = "O fóton será absorvido pelo átomo." \
                   "\n\nO nível final é {}."
        return ["Resultado", Resposta.format(result[1])]
    else:
        return result