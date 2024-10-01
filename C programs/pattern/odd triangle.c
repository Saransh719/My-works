#include<stdio.h>
int main()
{
    int h,i,p,j;
    printf("Enter height:");
    scanf("%d",&h);
    for (i=1;i<=h;i++)
    {
        p=1;
        for (j=1;j<=i;j++)
        {
            printf("%d",p);
            p+=2;
        }
        printf("\n");
    }
}