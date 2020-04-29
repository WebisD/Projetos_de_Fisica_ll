import energiaCinetica as eC
import energiaPotencial as eP
import energiaTotal as eT
import raioOrbita as rO

def getInput(n):
    print(n)
    try:
        value = float(n.replace(',','.'))
    except ValueError:
        return ["Error", "Não foi possivel interpretar o valor digitado como um numero"]

    print(value)
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
        return ["Success", Resposta.format(E_Cinetica, E_Potencial, E_Total, R_Orbita)]
    else:
        return ["Error", "Digite um valor inteiro"]