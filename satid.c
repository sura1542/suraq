#include<stdio.h>
int main(){
    char a,b ;
    printf("Enter a : ");
    scanf("%c", &a);
    fflush(stdin);
    
    printf("Enter b : ");
    scanf("%c", &b);

    printf("\na = %c, b = %c\n",a,b);
    return 0 ;
}