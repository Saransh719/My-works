#include<stdio.h>
int main(){
int age;
printf("Enter");
scanf("%d",&age);
if(age>=120){
    printf("invalid");
}
else if(age<0){
    printf("Invalid");
}
else if(age>18){
    printf("Yes");
}
else{
    printf("No");
}
return 0;
}
