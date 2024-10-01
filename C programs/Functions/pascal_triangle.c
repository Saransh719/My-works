#include<stdio.h>
int fact(int num)
{
    int prod=1;
    while (num>0)
    {
        prod*=num;
        num--;
    }
    return (prod);
}

int ncr(int n,int r)
{
    int fact(int);
    int ncr;
    ncr=(fact(n)/fact(r)/fact(n-r));
    return (ncr);
}

void main()
{
    int height,numbers,middle,i,j,pr=0,previous=0,next=0,space=1;
    printf("Enter height:");
    scanf("%d",&height);
    numbers=2*height-1;
    middle=numbers/2+1;
    for (i=1;i<=7;i++)
    {
        pr=0;
        space=1;
        for (j=1;j<=numbers;j++)
        {
            if ((j<middle-previous)||(j>middle+next)) printf(" ");
            else
            {
                if (space==1)
                {
                    printf("%d",ncr(i-1,pr));
                    pr++;
                    space=0;
                }
                else
                {
                    printf(" ");
                    space=1;
                }
            }
        }
        previous++; next++;
        printf("\n");
    }

}