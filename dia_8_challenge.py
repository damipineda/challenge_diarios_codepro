import random

def generador(length):
    if length < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return None

    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789*+-/@_?![]{}(),;.<~°^&$#\""
    contraseña = "".join(random.choice(caracteres) for _ in range(length))
    return contraseña

def main():
    while True:
        try:
            length = int(input("Introduce la longitud de la contraseña (mínimo 8 caracteres): "))
            contraseña = generador(length)
            if contraseña:
                print(f"Tu contraseña es: {contraseña}")

            repeat = input("¿Quieres generar otra contraseña? (si/no): ").strip().lower()
            if repeat == "no" or repeat == "n":
                print("¡Gracias por usar el generador de contraseñas!")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    main()
