#include <stdio.h>

    //Program to reverse the digits of a number
int main(){
    int enteredNum = 0, reversedNum = 0, remainder = 0;
    // Start by asking the user to enter a number between 100 and 10,000
    printf("Enter number between 100 and 10000:\n");
    
    // Keep asking the user for a number between 100 and 10,000 until the user complies.
    while(enteredNum<100 || enteredNum>10000){
        scanf("%d", &enteredNum);
        
        // Check if the user has complied, prompt for new number
        if(enteredNum<100 || enteredNum>10000){
            printf("That is not a number between 100 and 10000. Please enter new number now:\n");
        }
    }
    
    //Get reversed integer
    while(enteredNum != 0){
        remainder = enteredNum % 10;
        reversedNum = reversedNum*10 + remainder;
        enteredNum = enteredNum/10;
    }
    
    // Then print on the screen the digits of that number in reverse order
    printf("Reversed  number:\t%d", reversedNum);



    return 0;
}