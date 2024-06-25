#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    // Mensaje de inicio del programa
    printf("\n  **  PROGRAMA PARA ORDENAR NUMEROS  **\n\n");
    
    // Declarar variable para el número de elementos a ordenar
    int numeros_a_ordenar;
    
    // Solicitar al usuario la cantidad de números a ordenar
    printf(" Cuantos numeros deseas ordenar:  ");
    scanf(" %d", &numeros_a_ordenar);
    
    // Solicitar al usuario los números a ordenar
    printf("\n  Ingresa los numeros que quieres ordenar...\n");
    
    // Declarar el array para almacenar los números
    int vector_numeros[numeros_a_ordenar];
    int i, j, k = 1;
    
    // Leer los números del usuario
    for(i = 0; i < numeros_a_ordenar; i++)
    {
        printf("  %dºnumero: ", k);
        scanf(" %d", &j);
        vector_numeros[i] = j;
        k++;
    }
    
    // Mostrar los números ingresados por el usuario
    printf("\n\n  Estos son los numeros que quieres ordenar:  \n");
    printf("  ");
    for(i = 0; i < numeros_a_ordenar; i++)
    {
        printf("%d  ", vector_numeros[i]);
    }
    
    // Ordenar los números utilizando el método de burbuja
    int x, y;
    for(i = 0; i < numeros_a_ordenar; i++)
    {
        for(j = i + 1; j < numeros_a_ordenar; j++)
        {
            x = vector_numeros[i] - vector_numeros[j];
            if(x > 0)
            {
                y = vector_numeros[j];
                vector_numeros[j] = vector_numeros[i];
                vector_numeros[i] = y;
            }
        }
    }
    
    // Mostrar los números ordenados
    printf("\n\n Tus numeros estarian ordenados de esta forma:  \n");
    printf("  ");
    for(i = 0; i < numeros_a_ordenar; i++)
    {
        printf("%d  ", vector_numeros[i]);
    }
    
    return 0;
}
