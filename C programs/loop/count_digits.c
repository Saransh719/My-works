#include <stdio.h>
int main()
{
    int num, count = 0;
    printf("ENTER :");
    scanf("%d", &num);
    while (num > 0)
    {
        count += 1;
        num /= 10;
    }
    printf("No of digits are %d", count);
    return 0;
}