#include<stdio.h>
int main(){
    int n=3;
    //exp 1 ? exp2 :exp3   
    // if exp1, then exp 2, else exp3
    n%2==0 ? printf("Even number") : printf("Odd number");
    return 0;
}