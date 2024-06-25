#include <iostream>
#include <string>

using namespace std;

#define Num_PALABRAS 3  // Definir el número de palabras a evaluar
#define LEN_PALABRAS 100  // Longitud máxima de las palabras (aunque no se usa)

int main() {
    string texto;  // Variable para almacenar la palabra ingresada
    int aux, igual, contador_palindromos = 0;  // Variables auxiliares y contador de palíndromos
    std::string palindromos[Num_PALABRAS];  // Array para almacenar los palíndromos encontrados

    for(int i = 0; i < Num_PALABRAS; i++) {
        aux = 0;
        igual = 0;
        cout << "Ingrese la palabra a evaluar: ";
        getline(cin, texto);  // Leer la palabra ingresada por el usuario

        // Comparar la palabra desde el final hacia el inicio
        for (int ind = texto.length() - 1; ind >= 0; ind--) {
            if (texto[ind] == texto[aux]) {
                igual++;  // Incrementar si los caracteres son iguales
            }
            aux++;
        }

        // Verificar si la palabra es un palíndromo
        if (texto.length() == igual) {
            cout << "La palabra ingresada es palíndromo!!" << endl;
            palindromos[contador_palindromos] = texto;  // Almacenar el palíndromo
            contador_palindromos++;  // Incrementar el contador de palíndromos
        } else {
            cout << "La palabra ingresada NO es palíndromo!!" << endl;
        }
    }

    // Mostrar los resultados de las palabras palíndromas
    cout << "Resultado de las palabras palíndromas: " << endl;
    for (int j = 0; j < contador_palindromos; j++) {
        cout << palindromos[j] << endl;  // Imprimir cada palíndromo encontrado
    }

    return 0;  // Terminar el programa
}
