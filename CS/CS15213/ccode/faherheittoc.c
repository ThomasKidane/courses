#include <stdio.h>

int main(){
    int c=0;
    for(int i=0;i<20;i++){
        c=i;
        printf("%d %d\n",c,(c*9)/5+32);
        
    }
}