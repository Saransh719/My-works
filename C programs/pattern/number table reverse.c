// 1234321
// 123 321
// 12   21
// 1     1

#include<stdio.h>
int main()
{
    int n,i,j,k,number,middle,next=0,previous=0,pvalue;
    printf("Enter rows:");
    scanf("%d",&n);
    middle=n;
    number=2*n-1;
    for (i=1;i<=n;i++)
    {
        pvalue=1;
        for (j=1;j<=number;j++)
        {
            if ((j<middle+next)&&(j>middle-previous)) printf(" ");
            else printf("%d",pvalue);
            if (j<middle) pvalue++;
            else pvalue--; 
        }
        next++;
        previous++;
        printf("\n");
    }
}