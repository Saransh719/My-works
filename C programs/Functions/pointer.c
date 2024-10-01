//used to store memory address of a variable
#include<stdio.h>
void main()
{
    int a=5;
    int* pointer=&a;
    int **pp=&pointer;        //this stores address of pointer, if int* is given instead of int** warning is given but no error
    printf("%p \n",pointer);  //%p is for location address
    printf("%d \n",*pointer);    //pointer ke andar jis variable ka address hai uski value bataao(due to *)
    *pointer=7;   //pointer jiski taraf point kar rha hai, uski value change
    printf("%d \n",a);
    printf("%p \n",pp);
    printf("%p \n",&pointer);
    printf("%d \n",**pp);         //** will give value of a, only one * will generate warning and not give right value as it points to the pointer made for a and not the value of a(i.e. the variable named pointer)(%p would be required if one *)
    printf("%p \n",*pp);
    // any number of pointers can be made like this
} 