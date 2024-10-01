#include<stdio.h>
int main()
{
    int n,i,j1,j2;
    printf("Enter height:");
    scanf("%d",&n);
    for (i=1;i<=n;i++)
    {
        if (i%2!=0)
        {
           for (j1=1;j1<=i;j1++)
        {
            printf("%d",j1);
        } 
        }
        else
        {
            for (j2=1;j2<=i;j2++)
        {
            printf("%c",(char)(j2+64));
        }
        }
        printf("\n");
    }
}