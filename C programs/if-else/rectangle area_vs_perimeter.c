#include<stdio.h>
int main(){
    int l,b,p,a;
    printf("Enter lenght:");
    scanf("%d",&l);
    printf("Enter breadth:");
    scanf("%d",&b);
    p=2*(l+b);
    a=l*b;
    if (p>=a)
        printf("No area is not bigger than perimeter");
    else
        printf("Area is bigger than perimenter");
    return 0;
}