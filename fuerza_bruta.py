# Importa sólo el alfabeto en minúsculas/aunque no distingue entre min y mayúsculas desde el módulo string ascii
from string import ascii_lowercase

# Define una función llamada "fuerza_bruta" que toma una contraseña como argumento
def fuerza_bruta(password):
    # Contador para el número de intentos
    intentos = 0
    # Calcula la longitud de la contraseña
    longitud_password = len(password)
    # Define un conjunto de letras que serán utilizadas para generar las combinaciones
    letras = ascii_lowercase

    # Itera sobre las letras del alfabeto hasta encontrar la primera letra de la contraseña
    for letra in letras:
        # Incrementa el contador de intentos
        intentos += 1
        # Si la letra actual coincide con la primera letra de la contraseña, detiene la iteración
        if letra == password[0]:
            break

    # Itera sobre el resto de letras de la contraseña
    for i in range(1, longitud_password):
        # Itera sobre las letras del alfabeto
        for letra in letras:
            # Incrementa el contador de intentos
            intentos += 1
            # Si la letra actual coincide con la letra de la contraseña en la posición i, detiene la iteración
            if letra == password[i]:
                break

    # Devuelve el número total de intentos realizados
    return intentos

# El script es ejecutado directamente
if __name__ == "__main__":
    # Solicita al usuario ingresar una contraseña y la convierte a minúsculas con .lower()=minuscular
    """minuscular!= capitalizar"""
    password = input("Ingrese la contraseña: ").lower()
    # Llama a la función fuerza_bruta para contar el número de intentos necesarios para adivinar la contraseña
    intentos = fuerza_bruta(password)
    # Imprime el número total de intentos realizado
