#include<stdio.h>
int main()
{
    int num,sum=0,digit;
    printf("ENTER :");
    scanf("%d",&num);
    while (num>0)
    {
        digit=num%10;
        if (digit%2==0) 
        sum+=digit;
        num/=10;
    }
    printf("Sum of digits is %d",sum);
    return 0;
}