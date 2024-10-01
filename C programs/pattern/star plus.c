//     *
//  *  *  *
//     * 
//to print this, we can see that at i or j=(n+1)/2, * is printing
#include<stdio.h>
int main()
{
    int n,i,p,j;
    printf("Enter rows:");
    scanf("%d",&n);
    for (i=1;i<=n;i++)
    {
        for (j=1;j<=n;j++)
        {
           if ((i==(n+1)/2)||(j==(n+1)/2))
           {
            printf("* ");
           }
           else
           {
            printf("  ");
           }
        }
        printf("\n");
    }
}