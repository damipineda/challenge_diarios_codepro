#Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.

def contar_Vocales(caracteres): #Funcion para reconocer las vocales
    vocales = "aeiouAEIOU" #Variable que define las vocales en minúscula y mayúscula
    
    return sum(1 for char in caracteres if char in vocales) #Retorna la suma de 1 por cada vocal encontrada en la cadena

caracteres = input("Ingresa una palabra o frase: ") #Se solcita una frase o palabra al usuario" a "Se solicita una frase o palabra al usuario.

numero_vocales = contar_Vocales(caracteres) #Variable que contiene el número de vocales en la palabra/frase del usuario

print(f"El numero de vocales es: {numero_vocales}") #Se imprime el número de vocales