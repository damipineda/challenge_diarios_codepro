#Ordenar Lista: Escribe un programa que ordene una lista de números dada por el usuario en orden ascendente.
lista_numero = [] #Variable que crea una lista vacia
for i in range(5): #For que con un parametro de 5 
    ingreso = input('Ingresa un numero:  ') #Repite el input 5 veces
    lista = int(ingreso) #La lista se convierte en un entero
    lista_numero.append(lista) #Se agrega los ingresos del input a la lista

lista_numero.sort() #El punto sort() ordena la lista de menor a mayor
print(lista_numero) #Imprime la lista de menor a mayor