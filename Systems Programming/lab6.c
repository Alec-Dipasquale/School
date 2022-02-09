#include <stdio.h>
#include <math.h>

#define PI 3.14159

int main(){
        //declare variables
        float d1, d2, thickness, density;
        float rim, weight, batchweight;
        int numwashers;
        int *pointerNumWashers;

        //declare pointers
        float *pointerDi1, *pointerDi2, *pointerRim, *pointerWeight, *pointerThickness, *pointerDensity, *pointerBatchWeight,
        **pointToPointRim, **pointToPointWeight, **pointToPointBatchWeight;

        //initialize pointer to pointers for outputs
        pointToPointRim = &pointerRim;
        pointToPointWeight = &pointerWeight;
        pointToPointBatchWeight = &pointerBatchWeight;

        //initialize diameter pointers
        pointerDi1 = &d1;
        pointerDi2 = &d2;
        pointerRim = &rim;
        pointerThickness = &thickness;
        pointerDensity = &density;
        pointerNumWashers = &numwashers;
        pointerWeight = &weight;
        pointerBatchWeight = &batchweight;


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
        *pointerRim = ((*pointerDi2/2)*(*pointerDi2/2)*PI)-((*pointerDi1/2)*(*pointerDi1/2)*PI);
        //calculate the weight
        *pointerWeight = (*pointerRim)*(*pointerThickness)*(*pointerDensity);
        //calculate the batchweight
        *pointerBatchWeight = (*pointerWeight)*(*pointerNumWashers);

        //output the calculated results using pointer to pointers
        printf("\nrim area=%-10.5f square centimeters\n", **pointToPointRim);
        printf("weight of a washer=%-10.5f grams \n", **pointToPointWeight);
        printf("weight of all washers=%-10.5f grams \n", **pointToPointBatchWeight);
        return 0;
}
