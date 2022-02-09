

package fundamentals_of_programming.Lab1;

import java.math.RoundingMode;
import java.text.DecimalFormat;
import java.util.HashSet;
import java.util.Random;
import java.util.Set;
import java.util.concurrent.ThreadLocalRandom;

public class RandomSet {
    // class variable
    final String lexicon = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345674890";

    final java.util.Random rand = new java.util.Random();

    // consider using a Map<String,Boolean> to say whether the identifier is being used or not
    final Set<String> identifiers = new HashSet<String>();


    public String randomIdentifier() {
        Random generate = new Random();
        String[] name = {"John", "Marcus", "Susan", "Henry", "Serg", "David", "Alec", "Jeffrey", "Joey", "Jill", "Jerome",
                "Viktor", "Irene", "Sandy", "Jacob",
                "Ayaz", "Mysha", "Aidan", "Monty", "Shayaan", "Ritik", "Cruz"};
        return name[generate.nextInt(22)];
    }
    public String randomGradeLevelString(){
        int randomGradeLevelInt = ThreadLocalRandom.current().nextInt(1, 5);
        String randomGradeLevel = "";
        switch (randomGradeLevelInt) {

            case 1: randomGradeLevel = "freshman";
                break;
            case 2: randomGradeLevel = "sophomore";
                break;
            case 3: randomGradeLevel = "junior";
                break;
            case 4: randomGradeLevel = "senior";
                break;
        }
        return randomGradeLevel;
    }
    public int randomAge(){
        return ThreadLocalRandom.current().nextInt(17, 29);
    }
    public float randomGPA(){
        float randomNum = ThreadLocalRandom.current().nextFloat();
        randomNum = 2f + randomNum * (2f - 0f);
        DecimalFormat df = new DecimalFormat("#.###");
        df.setRoundingMode(RoundingMode.CEILING);
        randomNum = Float.parseFloat(df.format(randomNum));
        return randomNum;
    }
}
