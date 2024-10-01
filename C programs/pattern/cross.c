#include<stdio.h>
int main()
{
    int n,i,j;
    printf("Enter rows:");
    scanf("%d",&n);
    for (i=1;i<=n;i++)
    {
        for (j=1;j<=n;j++)
        {
           if ((i==j)||(j==n-i+1))  //can also use i+j=n+1 same logic
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