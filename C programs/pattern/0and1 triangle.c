// 1
// 01
// 101
// 0101     //each odd line is starting with 1 and even line is starting with 0
#include<stdio.h>
int main()
{
    int n,i,j,a;
    printf("Enter rows:");
    scanf("%d",&n);
    for (i=1;i<=n;i++)
    {
        if (i%2==0) a=0;
           else a=1;
        for (j=1;j<=i;j++)
        {
           printf("%d",a);
           if (a==1) a=0;
           else a=1;
        }
        printf("\n");
    }
}