//1-2+3-4......n
#include<stdio.h>
#include<math.h>
int main()
{
    int n,i,sum=0;
    printf("Enter n:");
    scanf("%d",&n);
    for (i=1;i<=n;i++)
    {
        sum+=pow(-1,i+1)*i;
    }
    printf("sum is %d",sum);
}