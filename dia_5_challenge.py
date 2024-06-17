
lista_1 = input("Ingresa una lista: ") # se socilicita al ausuario 2 listas
lista_2 = input("Ingresa otra lista: ")

lista1 = lista_1.split() #Con el .spit() se crea una lista a partir de la cadena ingresada por el usuario
lista2 = lista_2.split()
    
diccionario = dict(zip(lista1, lista2)) #Se convierte las lista en  diccionario

print(diccionario) #Se imprime el diccionario
