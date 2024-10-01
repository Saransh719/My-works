#include<stdio.h>
int main(){
    int cp,sp;
    printf("Enter CP:");
    scanf("%d",&cp);
    printf("Enter SP:");
    scanf("%d",&sp);
    if (cp>sp)
        printf("It is a loss of ₹%d",cp-sp);
    else if (sp>cp)
        printf("It is a profit of ₹%d",sp-cp);
    else
        printf("No profit no loss");
    return 0;
}