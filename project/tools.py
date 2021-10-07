def numero_to_letras(numero):

    indicador = [("", ""), ("MIL", "MIL"), ("MILLON", "MILLONES"),
                 ("MIL", "MIL"), ("BILLON", "BILLONES")]
    entero = int(numero)
    decimal = int(round((numero - entero)*100))
    contador = 0
    numero_letras = ""
    while entero > 0:
        a = entero % 1000
        if contador == 0:
            en_letras = convierte_cifra(a, 1).strip()
        else:
            en_letras = convierte_cifra(a, 0).strip()
        if a == 0:
            numero_letras = en_letras+" "+numero_letras
        elif a == 1:
            if contador in (1, 3):
                numero_letras = indicador[contador][0]+" "+numero_letras
            else:
                numero_letras = en_letras+" " + \
                    indicador[contador][0]+" "+numero_letras
        else:
            numero_letras = en_letras+" " + \
                indicador[contador][1]+" "+numero_letras
        numero_letras = numero_letras.strip()
        contador = contador + 1
        entero = int(entero / 1000)
    if (decimal > 10):
        decimal = str(decimal)
    else:
        decimal = '0'+str(decimal)
    numero_letras = numero_letras+" " + str(decimal) + "/100 BOLIVIANOS"
    return(numero_letras)

def convierte_cifra(numero, sw):
    lista_centana = ["", ("CIEN", "CIENTO"), "DOSCIENTOS", "TRESCIENTOS", "CUATROCIENTOS",
                     "QUINIENTOS", "SEISCIENTOS", "SETECIENTOS", "OCHOCIENTOS", "NOVECIENTOS"]
    lista_decena = ["", ("DIEZ", "ONCE", "DOCE", "TRECE", "CATORCE", "QUINCE", "DIECISEIS", "DIECISIETE", "DIECIOCHO", "DIECINUEVE"),
                    ("VEINTE", "VEINTI"), ("TREINTA",
                                           "TREINTA Y "), ("CUARENTA", "CUARENTA Y "),
                    ("CINCUENTA", "CINCUENTA Y "), ("SESENTA",
                                                    "SESENTA Y "),
                    ("SETENTA", "SETENTA Y "), ("OCHENTA",
                                                "OCHENTA Y "),
                    ("NOVENTA", "NOVENTA Y ")
                    ]
    lista_unidad = ["", ("UN", "UNO"), "DOS", "TRES",
                    "CUATRO", "CINCO", "SEIS", "SIETE", "OCHO", "NUEVE"]
    centena = int(numero / 100)
    decena = int((numero - (centena * 100))/10)
    unidad = int(numero - (centena * 100 + decena * 10))
    texto_centena = ""
    texto_decena = ""
    texto_unidad = ""
    texto_centena = lista_centana[centena]
    if centena == 1:
        if (decena + unidad) != 0:
            texto_centena = texto_centena[1]
        else:
            texto_centena = texto_centena[0]
    texto_decena = lista_decena[decena]
    if decena == 1:
        texto_decena = texto_decena[unidad]
    elif decena > 1:
        if unidad != 0:
            texto_decena = texto_decena[1]

        else:
            texto_decena = texto_decena[0]
    if decena != 1:
        texto_unidad = lista_unidad[unidad]
        if unidad == 1:
            texto_unidad = texto_unidad[sw]
    return "%s %s %s" % (texto_centena, texto_decena, texto_unidad)




def date(fecha):
    print(fecha)
    meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Octubre","Noviembre","Diciembre")
    dias = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
    year = fecha.year
    mes = meses[fecha.month - 1]
    dia = dias[fecha.weekday()]
    message = f"{dia} {fecha.day} de {mes} de {year}"
    print(message)
    return message