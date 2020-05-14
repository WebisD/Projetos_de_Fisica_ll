import constantes

def multiplicadorR(n1, n2):
    valor = (1/(n1**2)) - (1/(n2**2))
    return valor

def calcComprimentoComSerie(n, serie):
    comprimento = 0.0
    possiveisN = {"Lyman": "2, 3, 4,...",
                  "Balmer": "3, 4, 5,...",
                  "Paschen": "4, 5, 6...",
                  "Brackett": "5, 6, 7...",
                  "Pfund" : "6, 7, 8..."
                  }
    cor = ""

    if serie == "Lyman" and n >= 2:
        possiveisN = "2, 3, 4,..."
        comprimento = 1/(constantes.R * multiplicadorR(1, n))
        cor = "Ultravioleta"
    elif serie == "Balmer" and n >= 3:
        possiveisN = "3, 4, 5,..."
        comprimento = 1/(constantes.R * multiplicadorR(2, n))
        #definir a cor no espectro de Balmer
    elif serie == "Paschen" and n >= 4:
        possiveisN = "4, 5, 6..."
        comprimento = 1/(constantes.R * multiplicadorR(3, n))
        cor = "Infravermelho"
    elif serie == "Brackett" and n >= 5:
        possiveisN = "5, 6, 7..."
        comprimento = 1/(constantes.R * multiplicadorR(4, n))
        cor = "Infravermelho"
    elif serie == "Pfund" and n >= 6:
        possiveisN = "6, 7, 8..."
        comprimento = 1/(constantes.R * multiplicadorR(5, n))
        cor = "Infravermelho"
    else:
        return "Error","Para a serie de " + serie + " os valores válido são: " + possiveisN[serie]
    

    return comprimento, cor