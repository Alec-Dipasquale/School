#include <stdio.h>
#include <math.h>

#define PI 3.14159

int main(){
        //declare variables
        float d1, d2, thickness, density;
        float rim, weight, batchweight;
        int numwashers;

        //Ask user for and store inputs
        printf("What is the inner diameter in centimeters?\n");
        scanf("%f", &d1);
        printf("What is the outer diameter in centimeters?\n");
        scanf("%f", &d2);
        printf("What is the thickness in centimeters?\n");
        scanf("%f", &thickness);
        printf("What is the material density in grams/cm^3?\n");
        scanf("%f", &density); //Number in the batch?
        printf("How many washers do you have?\n");
        scanf("%i", &numwashers);

        //calculate rim
        rim = ((d2/2)*(d2/2)*PI)-((d1/2)*(d1/2)*PI);
        //calculate the weight
        weight = rim*thickness*density;
        //calculate the batchweight
        batchweight = weight*numwashers;

        //output the calculated results
        printf("\nrim area=%-10.5f square centimeters\n", rim);
        printf("weight of a washer=%-10.5f grams \n", weight);
        printf("weight of all washers=%-10.5f grams \n", batchweight);
        return 0;
}
