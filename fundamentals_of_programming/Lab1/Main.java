package fundamentals_of_programming.Lab1;
/*
To understand the value of records in a programming language, write a small
program in a C-based language ( C, C++, C#, Java, R) that uses an array of
structs/objects that store student information, including name, age, GPA as
a float, and grade level as a string (e.g., freshmen, etc.) Also, write the
same program in the same language without using structs/objects. For instance,
you can create a student info array, prompt the user to enter the data values
of each student, or initialize the array of structure, then print all student
info. Users should also be able to print students in certain grade levels,
say print all-freshman student info. Think of another function, such as the
search for a particular name, GPA above a certain value, etc. Try to have
at least two student processing functions. The program can prompt the user
to enter their function choices.
*/
import java.util.Scanner;

public class Main {
    private final static int numOfStudents = 30;

    public static void main(String[] args) {
        RandomSet randomSetObj = new RandomSet();
        String students[][] = new String[numOfStudents][4];
        Scanner scan = new Scanner(System.in);
        //init array of student info
        for (int i = 0; i < numOfStudents; i++) {

            students[i][0] = String.valueOf(randomSetObj.randomAge());
            students[i][1] = randomSetObj.randomGradeLevelString();
            students[i][2] = randomSetObj.randomIdentifier();
            students[i][3] = String.valueOf(randomSetObj.randomGPA());
        }

        //print all student info
        for (int i = 0; i < numOfStudents; i++) {
            System.out.println("Name:\t" + students[i][2] + "\tAge:\t" + students[i][0] +
                    "\tGrade Level:\t" + students[i][1] + "\tGPA:\t" + students[i][3]);
        }
        int functionChoice = -1;
        while (functionChoice != 0) {
            System.out.println("How would you like to search\n'1' = by grade level\t '2' = by minimum gpa\t'0' = exit");
            functionChoice = scan.nextInt();
            switch (functionChoice) {
                case 1:
                    System.out.println("\nWhat grade level are you searching for?\nfreshman\tsophomore\tjunior\tsenior");
                    String inputGradeLevel = scan.next();
                    printGradeLevelStudents(inputGradeLevel, students);
                    break;
                case 2:
                    System.out.println("\nWhat is the minimum GPA you want to search for?\t##.###");
                    float inputGPA = scan.nextFloat();
                    printGpaAbove(inputGPA, students);
                    break;
                case 0:
                    break;
            }
        }
    }
        //prints all students within a user indicated grade level
        public static void printGradeLevelStudents(String gradeLevelString, String students[][]){
            for (int i = 0; i < numOfStudents; i++) {
                if (gradeLevelString.equalsIgnoreCase(students[i][1])) {
                    System.out.println("Name:\t" + students[i][2] + "\tAge:\t" + students[i][0] +
                            "\tGrade Level:\t" + students[i][1] + "\tGPA:\t" + students[i][3]);
                }
            }
        }

        //prints all students above a user indicated gpa
        public static void printGpaAbove ( float minGpa, String students[][]){
            for (int i = 0; i < numOfStudents; i++) {
                if (Float.parseFloat(students[i][3]) > minGpa) {
                    System.out.println("Name:\t" + students[i][2] + "\tAge:\t" + students[i][0] +
                            "\tGrade Level:\t" + students[i][1] + "\tGPA:\t" + students[i][3]);
                }
            }
        }
}