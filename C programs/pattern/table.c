// *******
// *** ***
// **   **
// *     * 
#include<stdio.h>
int main()
{
    int n,i,j,k,space=0,star;
    printf("Enter rows:");
    scanf("%d",&n);
    star=2*n-1;
    for (i=1;i<=n;i++)
    {
        for (j=1;j<=star;j++) printf("*");
        for (k=1;k<=space;k++) printf(" ");
        for (j=1;j<=star;j++) printf("*");
        star--;
        space+=2;
        printf("\n");
    }
}