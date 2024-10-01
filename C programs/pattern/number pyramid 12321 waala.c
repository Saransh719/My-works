//    1
//   121
//  12321
// 1234321   divide this into 2 parts, one is 1,12,123 and other is 1,21,321
#include<stdio.h>
int main()
{
    int n,i,j,k,s;
    printf("Enter rows:");
    scanf("%d",&n);
    for (i=1;i<=n;i++)
    {
        for (s=n-i;s>=1-1;s--)
        {
            printf(" ");
        }
        for (j=1;j<=i;j++)
        {
            printf("%d",j);
        }
        for (k=i-1;k>=1;k--)
        {
            printf("%d",k);
        }
        printf("\n");
    }
}