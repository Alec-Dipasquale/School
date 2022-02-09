#include <stdio.h>
#include <math.h>

int calculateNumRecurs(int num);
int calculateNum(int num);

int main(){
        int num = -1, result =0;
        char recurs;
        while(num>15 || num <1 ){
                printf("Please enter an integer between 1 and 15.\n");
                scanf("%d", &num);
        }

        printf("Enter 'y' if you would like recursion\n");
        scanf(" %c", &recurs);
        if(recurs == 'y'){
                result = calculateNumRecurs(num);
        }else{
                result = calculateNum(num);
        }

        printf("%d! equals %d\n", num, result);
        return 0;
}

int calculateNumRecurs(int num){
        if(num > 1){
                return  num * calculateNumRecurs(num-1);
        }else{
                return num;
        }
}

int calculateNum(int num){
        int result = 1;
        while( num > 1){
                result = result * num;
                num = num -1;
        }
        return result;
}
