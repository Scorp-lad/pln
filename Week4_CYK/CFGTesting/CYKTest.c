#include <stdio.h>

/*
    This program is just the testing code.
    You should run the other python code to see the CYK result instead.
*/
int main(){
    int i, j, k;
    for(i=2; i<=4; i++){
        for(j=1; j<=5-i; j++){
            for(k=0; k<i-1; k++){
                printf("( %d , %d ) += B[ ( %d , %d) * ( %d , %d ) ]\n",
                j, i, j, k+1, j+k+1, i-k-1);
            }
        }
        printf("\n");
    }
}