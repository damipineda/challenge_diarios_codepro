#Se crea una funcion para mostra la tabla de multiplicar

def tabla_multiplicar(numero):
    for i in range(1, 13):
        print(str(numero) + " x " + str(i) + " = " + str(numero * i))
        
#Input para solircitar numero al usuario

numero = int(input("Ingresa un numero:  "))

#Impimir la tabla de multipicar

print("La tabla de multiplicar  " + str(numero) + '  es :')

tabla_multiplicar(numero)