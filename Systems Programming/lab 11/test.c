#include <stdio.h>

int main(int argc, char *argv[]){
    char buffer[1024] = "";
    for(;;){
        fgets(buffer, 1024, stdin);

        if(strncmp(buffer, "exit", 4) == 0) break;
        printf("buffer: %s\n", buffer);
    }
    return 0;
}