#include<stdio.h>
main(){
    int a,b,r;
    char c;
    scanf("%d %c %d",&a,&c,&b);
    switch(c){
        case '+':{
            r=a+b;
            break;
        }
        case '-':{
            r=a-b;
            break;
        }
    }
    printf("%d",r);
}