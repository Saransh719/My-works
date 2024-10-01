// sum of cube of digits=number
#include <stdio.h>
#include <math.h>
int main()
{
    int num, sum = 0,digit;
    printf("ENTER :");
    scanf("%d", &num);
    int temp = num;
    while (temp > 0)
    {
        digit = temp % 10;
        sum += pow(digit, 3);
        temp/=10;
    }
    if (sum==num) printf("Number is armstrong");
    else printf("Number is not armstrong");
    return 0;
}