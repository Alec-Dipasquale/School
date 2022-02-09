import java.text.NumberFormat;
import java.util.ArrayList;

public class Order {
	private double total;
	private ArrayList<Pizza> orderList = new ArrayList<>();
	private ArrayList<Toppings> orderToppings = new ArrayList<>();

	private Toppings toppings;
	NumberFormat usDollars = NumberFormat.getCurrencyInstance();
	
	
	public Order(){
		this.total = 0.0;
	}
	
	public void addPizza(Pizza p){
		p.setCost();
		this.total += p.getCost();
		orderList.add(p);
	
	}

	public void addToppings(Toppings t){
		t.setCost();
		this.total +=t.getCost();
		orderToppings.add(t);
	}
	
	public String toString(){
		String strOrder = "";
		for(int i = 0; i< orderList.size() || i<orderToppings.size(); ++i){
			if(i<orderList.size()) {
				strOrder += "Pizza #" + (i + 1) + "\n";
				strOrder += orderList.get(i).toString();
				strOrder += "************************\n";
				strOrder += "Toppings:\n";
			}
			if(i<orderToppings.size()) {
				strOrder += orderToppings.get(i).toString();
				strOrder += "************************\n";
			}
		}
		strOrder += "Sub Total: " + usDollars.format(this.total);
		return strOrder;
	}
	
	public String finalBill(){
		String bill = this.toString();
		bill += "\nTax 7%:" + usDollars.format(this.total * .07);
		bill += "\nFinal Total: " + usDollars.format(this.total * 1.07);
		return bill;
	}
	
}
