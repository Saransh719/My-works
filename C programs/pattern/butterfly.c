#include<stdio.h>
int main()
{
    int n,i,j,k=1,middle;
    printf("Enter rows:");
    scanf("%d",&n);
    middle=n/2;
    for (i=1;i<=n;i++)
    {
        for (j=1;j<=n;j++)
        {
            if ((j<=k)||(j>(n-k))) 
            {
                printf("* ");
            }
            else 
            {
                printf("  ");
            }
        }
        printf("\n");
        if (i<middle) k++;
        else if(i>middle) k--;
        else continue;               //not necessary, just wrote if further adjustments are needed
    }
}