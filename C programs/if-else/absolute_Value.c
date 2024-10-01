#include<stdio.h>
int main(){
    int a,na;
    printf("Enter integer:");
    scanf("%d",&a);
    na=a;
    if (a<0)
        na=-a;
    printf("Absolute value of %d is %d",a,na);
}