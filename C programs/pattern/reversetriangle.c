#include<stdio.h>
int main()
{
    int n,i,j,k;
    printf("Enter rows:");
    scanf("%d",&n);
    // for (i=n;i>=1;i--)
    // {
    //     for (j=1;j<i;j++)
    //     {
    //         printf(" ");
    //     }
    //     for (k=1;k<=n-j+1;k++)
    //     {
    //         printf("*");
    //     }
    //     printf("\n");
    // }
    //better code
    for (i=1;i<=n;i++)
    {
        for (j=1;j<=n-i;j++)
        {
            printf(" ");
        }
        for (k=1;k<=i;k++)
        {
            printf("*");
        }
        printf("\n");
    }

}