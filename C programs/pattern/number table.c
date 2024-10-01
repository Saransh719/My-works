// 1234567
// 123 567
// 12   67
// 1     7

#include<stdio.h>
int main()
{
    int n,i,j,k,number,middle,next=0,previous=0;
    printf("Enter rows:");
    scanf("%d",&n);
    middle=n;
    number=2*n-1;
    for (i=1;i<=n;i++)
    {
        for (j=1;j<=number;j++)
        {
            if ((j<middle+next)&&(j>middle-previous)) printf(" ");
            else printf("%d",j);
        }
        next++;
        previous++;
        printf("\n");
    }
}