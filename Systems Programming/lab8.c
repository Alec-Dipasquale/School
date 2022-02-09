#include <stdio.h>
#include <stdlib.h>
#include <math.h>


//structure for holding graph points and name
struct Graphs {
    double xCoord;
    double yCoord;
    char graph_name[100];
};


int main(){

    //init of variables
    struct Graphs graphs[100];
    int numOfCoordinates;
    char closestPoints1[100], closestPoints2[100], furthestPoints1[100], furthestPoints2[100], tempDouble[10], *ptr;
    double xCoord, yCoord, closestD = -1, furthestD = -1, distance;

    //prompt for how many coordinates needed.
    printf("Please input the number of coordinates:\n");
    fgets(tempDouble, 10, stdin);
    numOfCoordinates  = atoi(tempDouble);

    //loop to get each coordinate point and find the closest and furthest distances.
    for(int i = 0; i < numOfCoordinates; i++){
        
        //prompts for coordinate point
        printf("Please enter label for coordinate:\n");
        fgets(graphs[i].graph_name, 100, stdin);
         for(int j = 0; j < i; j++){
            if(strcmp(graphs[i].graph_name, graphs[j].graph_name) == 0){
                printf("Please enter a name not used:\n");
                fgets(graphs[i].graph_name, 100, stdin);
                j = 0;
            }
        }
        printf("Please enter x coordinate:\n");
        fgets(tempDouble, 10, stdin);
        graphs[i].xCoord = strtod(tempDouble, &ptr);
        printf("Please enter y coordinate:\n");
        fgets(tempDouble, 10, stdin);
        graphs[i].yCoord = strtod(tempDouble, &ptr);
        

        //Pythagorean theorem ((x_2-x_1)²+(y_2-y_1)²)
        if(i > 0){
            for(int j = i-1; j >= 0; j--){

                distance = sqrt( pow(graphs[i].xCoord - graphs[j].xCoord, 2) + pow(graphs[i].yCoord - graphs[j].yCoord, 2) );

                if(distance <= closestD || closestD == -1){
                    closestD = distance;
                    strcpy(closestPoints1, graphs[i].graph_name);
                    strcpy(closestPoints2, graphs[j].graph_name);
                }
                if(distance >= furthestD || furthestD == -1){
                    furthestD = distance;
                    strcpy(furthestPoints1, graphs[i].graph_name);
                    strcpy(furthestPoints2, graphs[j].graph_name);
                }
            }
        }
    }
    closestPoints1[strlen(closestPoints1) - 1] = '\0';
    closestPoints2[strlen(closestPoints2) - 1] = '\0';
    furthestPoints1[strlen(furthestPoints1) - 1] = '\0';
    furthestPoints2[strlen(furthestPoints2) - 1] = '\0';
    printf("The two closest coordinates are:\t%s and %s with a distance of %lf\n", closestPoints1, closestPoints2, closestD);
    printf("The two furthest coordinates are:\t%s and %s with a distance of %lf\n", furthestPoints1, furthestPoints2, furthestD);

    
    return 0;
}