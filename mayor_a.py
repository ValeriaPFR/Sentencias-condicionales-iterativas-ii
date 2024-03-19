# Importar el módulo sys, que se utilizará para acceder a los argumentos de la línea de comandos
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
''' Esta función recorre el diccionario y encuentra los valores mayores al umbral recibido '''
def obtener_meses_mayor_a_umbral(umbral):
        # Inicializa un diccionario vacío {} para almacenar los meses con ventas mayores al umbral
    meses_mayor_a_umbral = {}
    # Itera sobre cada par clave:valor en el diccionario de ventas
    for mes, valor in ventas.items():
        # Comprueba si el valor de ventas es mayor que el umbral recibido
        if valor > umbral:
            # Si es mayor, agrega el par clave:valor al diccionario meses_mayor_a_umbral
            meses_mayor_a_umbral[mes] = valor
    # Devuelve el diccionario con los meses y sus valores de ventas que superan el umbral
    return meses_mayor_a_umbral

# Convierte el primer argumento de la línea de comandos a un entero (int) , que representa el umbral de ventas
umbral = int(sys.argv[1])

# Llama a la función obtener_meses_mayor_a_umbral con el umbral proporcionado y almacena los resultados
resultados = obtener_meses_mayor_a_umbral(umbral)
