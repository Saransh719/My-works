//     *
//    ***
//   *****
//    ***
//     *          take cells and find mathematical equation    n is odd
// middle line is (n/2)+1 ==> n/2 spaces se start  // answer will be integer so dont worry
#include<stdio.h>
int main()
{
    int n,i,j,k,space,star=1;
    printf("Enter rows:");
    scanf("%d",&n);
    space=n/2;
    for (i=1;i<=n;i++)
    {
        for (j=1;j<=space;j++)
        {
            printf(" ");
        }
        if (i<(n/2)+1) space--;
        else space++;
        for (k=1;k<=star;k++)
        {
            printf("*");
        }
        if (i<(n/2)+1) star+=2;
        else star-=2;
        printf("\n");
    }

}