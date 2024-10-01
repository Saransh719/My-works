#include<stdio.h>
int main()
{
    int num,i;
    printf("Enter number:");
    scanf("%d",&num);
    for (i=2;i<num;i++)
    {
        if (num%i==0)
        {
            printf("Number is composite");
            break;
        }
    }
    if (i==num)
    {
        printf("Number is prime");
    }
    if (num==1) 
    {
        printf("1 is neither prime nor composite");
    }
    return 0;
}