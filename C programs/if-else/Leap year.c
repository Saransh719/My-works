#include<stdio.h>
int main(){
    int i;
    printf("Enter year:");
    scanf("%d",&i);
    if (i%400==0)
        printf("Leap year");
    else if ((i%100!=0) && (i%4==0))
        printf("Leap year");
    else
        printf("Not a leap year");
    return 0;

}