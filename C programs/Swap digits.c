#include<stdio.h>
#include<math.h>
int main(){
    int i,j,num,n,digit,temp,size,count;
    printf("Enter Number:");
    scanf("%d",&num);
    temp=num;
    count=0;
    while (temp>0)
    {
        temp=temp/10;
        count++;
    }
    int arr[count];
    printf("Enter i:");
    scanf("%d",&i);
    printf("Enter j:");
    scanf("%d",&j);
    n=0;
    while (num>0)
    {   
        digit=num%10;
        arr[n]=digit;
        n++;
        num=num/10;
    }
    size=sizeof(arr)/sizeof(arr[0]);
    temp=arr[i-1];
    arr[i-1]=arr[j-1];
    arr[j-1]=temp;
    for (n=0;n<size;n++)
    {
        num=num+(arr[n]*(pow(10,n)));
    }
    printf("New number is %d",num);
    return 0;
}
