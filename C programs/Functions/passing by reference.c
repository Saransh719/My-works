//when we pass by value(like we do usually) value of variable is not changed as we know, therefore to do that pass by reference
//swapping two numbers using functions
void swap(int* x,int* y)
{
    int temp;
    temp=*x;         //temp=3
    *x=*y;           // a=9
    *y=temp;         //b=3         //here, values of a and b were changed directly as we are changing the value of addresses
}
void main()
{
    int a=3,b=9;
    printf("a=%d \n b=%d",a,b);
}