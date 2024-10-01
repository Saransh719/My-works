#include<stdio.h>
int fact(int n)
{
    int prod=1;
    while (n>0)
    {
        prod*=n;
        n--;
    }
    return (prod);
}

void main()
{
    int n,r;
    printf("Enter n:");
    scanf("%d",&n);
    printf("Enter r:");
    scanf("%d",&r);
    printf("%dC%d =%d",n,r,(fact(n)/fact(r)/fact(n-r)));
}