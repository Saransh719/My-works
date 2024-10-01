#include<stdio.h>
void main()
{
    int m1,n1,m2,n2,i,j,k,temp=0;
    //taking all inputs and checking
    printf("Enter number of rows of 1st matrix :");
    scanf("%d",&m1);
    printf("Enter number of columns of 1st matrix :");
    scanf("%d",&n1);
    printf("Enter number of rows of 2nd matrix :");
    scanf("%d",&m2);
    printf("Enter number of columns of 2nd matrix :");
    scanf("%d",&n2);
    if (n1!=m2)
    {
        printf("Matrices cannot be multiplied");
        return;
    }
    int arr1[m1][n1],arr2[m2][n2],arr3[m1][n2];
    for (i=0;i<m1;i++)
    {
        for (j=0;j<n1;j++)
        {
            printf("Enter element of %d row and %d column for 1st matrix : ",i+1,j+1);
            scanf("%d",&arr1[i][j]);
        }
    }
    for (i=0;i<m2;i++)
    {
        for (j=0;j<n2;j++)
        {
            printf("Enter element of %d row and %d column for 2nd matrix : ",i+1,j+1);
            scanf("%d",&arr2[i][j]);
        }
    }
    //starting multiplication
    for (i=0;i<m1;i++)
    {
        for (j=0;j<n2;j++)
        {
            temp=0;
            for (k=0;k<n1;k++)
            {
                temp+=arr1[i][k]*arr2[k][j];
            }
            arr3[i][j]=temp;
        }
    }
    //printing new matrix
    for (i=0;i<m1;i++)
    {
        for (j=0;j<n2;j++)
        {
            printf("%d \t",arr3[i][j]);
        }
        printf("\n");
    }

}