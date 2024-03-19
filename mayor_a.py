import sys

# Definición del diccionario ventas, que contiene los datos de ventas mensuales
ventas = {
        "Enero": 15000,
        "Febrero": 22000,
        "Marzo": 12000,
        "Abril": 17000,
        "Mayo": 81000,
        "Junio": 13000,
        "Julio": 21000,
        "Agosto": 41200,
        "Septiembre": 25000,
        "Octubre": 21500,
        "Noviembre": 91000,
        "Diciembre": 21000,
}

def obtener_meses_mayor_a_umbral(umbral):
    ''' esta funcion recorre el diccionario y encuentra los valores mayores al umbral recibido'''
    meses_mayor_a_umbral = {}
    for mes, valor in ventas.items():
        if valor > umbral:
            meses_mayor_a_umbral[mes] = valor
    return meses_mayor_a_umbral


umbral = int(sys.argv[1])

resultados = obtener_meses_mayor_a_umbral(umbral)

