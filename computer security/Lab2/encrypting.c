#include <stdlib.h>

const char* myName();

int main(int argc, char **argv){
    char phrase[] = "This is the phrase to encrypt.";
    char key[] = "FLYING CAR";
    char encrypted[] = encrypt(key, phrase);

}

const char* encrypt(char key[], char msg[]) {
    char encrypted[strlen(msg)];
    int keyInc = 0;
    for(int i = 0; (i < 100 && msg[i] != '\0'); i++){
        keyInc = i % (int)strlen(key);
        encrypted[i] = msg[i] + (int)key[i]; //the key for encryption is 3 that is added to ASCII value
    }

      printf("\nEncrypted string: %s\n", encrypted);
    return encrypted;
}