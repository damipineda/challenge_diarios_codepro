#Dia 7
#Juego de Piedra, Papel o Tijeras: 
# Escribe un programa que permita al usuario jugar piedra, papel o tijeras contra la computadora.

import random 

opciones = ("piedra", "papel", "tijera") 

usuario = input("piedra, papel, tijera:  ") 
usuario = usuario.lower()
print(usuario)
computadora =  random.choice(opciones)

if not usuario in opciones:
    print("Opcion invalida")
    
print("Usuario =>", usuario)
print("Computadora =>", computadora)

if usuario == computadora:
    print("Es empate")
elif usuario =="piedra":
    if computadora == "tijera":
        print("Piedra gana a tijera")
        print("Usuario gano")
elif usuario == "papel":
    if computadora == "piedra":
        print("Papel gana a pierdra")
        print("Usuario gano")
    else:
        print("Tijera gana a papel")
        print("Gano la compuntadora")
elif usuario == "tijera":
    if computadora == "papel":
        print("Tijera gana a papel")
        print("Usuario gano")
    else:
        print("Piedra gana a tijera")
        print("Computadora gano")
