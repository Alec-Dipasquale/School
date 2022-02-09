import java.text.NumberFormat;
import java.util.ArrayList;

/**
 * Created by Alec on 4/27/2016.
 */
public class Toppings {
    private String type;
    private double cost;
    NumberFormat usDollars = NumberFormat.getCurrencyInstance();
    //private ArrayList<String> toppings = new ArrayList<>();

    public Toppings(){
        this.type = "plain";
        this.cost = 0.0;
    }
    public Toppings(String type){
        this.type = type;
    }


    public void setCost() {
        switch (this.type) {
            case ("Pepperoni"):
                this.cost = 2.50;
                break;
            case ("Sausage"):
                this.cost = 4.00;
                break;
            case ("Ham"):
                this.cost = 4.00;
                break;
            case ("Chicken"):
                this.cost = 4.50;
                break;
            case ("Beef"):
                this.cost = 4.50;
                break;
            case ("Yellow Peppers"):
                this.cost = 1.50;
                break;
            case ("Bell Peppers"):
                this.cost = 1.75;
                break;
            case ("Broccoli"):
                this.cost = 3.50;
                break;
            case ("Pineapple"):
                this.cost = 2.75;
                break;

            default:
                this.cost = 0.00;
                break;
        }
    }
    public double getCost(){
        return this.cost;
    }

    public String getStrTopping() {
        return this.type;
    }

    public String toString(){
        return "\t\t"+ this.getStrTopping() + ", Cost: " + usDollars.format(this.getCost());

    }
}
