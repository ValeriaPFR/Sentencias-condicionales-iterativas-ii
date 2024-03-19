from string import ascii_lowercase

def fuerza_bruta(password):
    intentos = 0
    longitud_password = len(password)
    letras = ascii_lowercase

    for letra in letras:
        intentos += 1
        if letra == password[0]:
            break

    for i in range(1, longitud_password):
        for letra in letras:
            intentos += 1
            if letra == password[i]:
                break

    return intentos

if __name__ == "__main__":
    password = input("Ingrese la contraseña: ").lower()
    intentos = fuerza_bruta(password)
    print(f"La contraseña fue forzada en {intentos} intentos")