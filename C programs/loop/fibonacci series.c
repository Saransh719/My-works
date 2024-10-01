#include<stdio.h>
int main()
{
    int n,i,p=1,pp=1,num=1;
    printf("Enter n:");
    scanf("%d",&n);
    for (i=1;i<=n;i++){
        if (i>2) break;
        printf("1 ");
    }
    for (i=3;i<=n;i++)
    {
        num=p+pp;
        pp=p;
        p=num;
        printf("%d ",num);
    }
}