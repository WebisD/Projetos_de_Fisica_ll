import constantes

def multiplicadorR(n1, n2):
    valor = (1/(n1**2)) - (1/(n2**2))
    return valor

def corEspectro(comp):
    cor = ""
    espectro = "Luz visível"

    if comp == 410.20966271649957:
        cor = "Violeta"
    elif comp == 434.084299170899:
        cor = "Azul"
    elif comp == 486.1744150714068:
        cor = "Verde"
    elif comp == 656.3354603463993:
        cor = "Vermelho"
    else:
        espectro = "Ultravioleta"

    return cor, espectro

def calcComprimentoComSerie(n, serie):
    comprimento = 0.0
    possiveisN = {"Lyman": "2, 3, 4,...",
                  "Balmer": "3, 4, 5,...",
                  "Paschen": "4, 5, 6...",
                  "Brackett": "5, 6, 7...",
                  "Pfund": "6, 7, 8..."
                  }

    cor = ""
    espectro = ""

    if serie == "Lyman" and n >= 2:
        possiveisN = "2, 3, 4,..."
        comprimento = 1/(constantes.R * multiplicadorR(1, n)) * 10**9
        espectro = "Ultravioleta"
    elif serie == "Balmer" and n >= 3:
        possiveisN = "3, 4, 5,..."
        comprimento = 1/(constantes.R * multiplicadorR(2, n)) * 10**9
        cor, espectro = corEspectro(comprimento)
    elif serie == "Paschen" and n >= 4:
        possiveisN = "4, 5, 6..."
        comprimento = 1/(constantes.R * multiplicadorR(3, n)) * 10**9
        espectro = "Infravermelho"
    elif serie == "Brackett" and n >= 5:
        possiveisN = "5, 6, 7..."
        comprimento = 1/(constantes.R * multiplicadorR(4, n)) * 10**9
        espectro = "Infravermelho"
    elif serie == "Pfund" and n >= 6:
        possiveisN = "6, 7, 8..."
        comprimento = 1/(constantes.R * multiplicadorR(5, n)) * 10**9
        espectro = "Infravermelho"
    else:
        return "Erro","Para a série de " + serie + " os valores válidos são: " + possiveisN[serie]

    return comprimento, cor, espectro