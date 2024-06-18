temperatura = float(input("Ingresa la temperatura actual: ")) #Se solicita la temperatura actual al usuario

def convertir_temperatura(temperatura): #Duncion para convertira la temperatura de GC a F
    return (temperatura * 9/5) + 32 #Formula para covertir GC aF
temperatura_F = convertir_temperatura(temperatura) #La funcion se llama a una varible
print(f"La teemperatura Fahrenheit es: {temperatura_F}") #Se imprime la temperatura convertida