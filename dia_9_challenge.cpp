//Programa que pide al usuario 2 numeros y los suma

#include <iostream>>
using namespace std;

int main(){
cout <<"Programa que pide al usuario/a dos numeros enteros y muestra la suma."<<endl;
int dato;
int suma = 0;

for (int i=0; i < 2; i=i+1){
cout<<"Ingresa un numero: ";
cin>>dato;
suma = suma + dato;
}
cout<<"La suma de los numeros ingesados es:  "<<suma << endl;

return 0;

}