import java.text.NumberFormat;

public class Pizza {
	private int size;
	private double cost;
	NumberFormat usDollars = NumberFormat.getCurrencyInstance();
	
	public Pizza(){
		size = 2;
		cost = 10.00;
	}
	
	public Pizza(int size){
		this.size = size;
	}
	
	public void setCost(){
		switch(this.size){
		case(1):
			this.cost = 8.00;
			break;
		case(2):
			this.cost = 10.00;
			break;
		case(3):
			this.cost = 14.00;
			break;
		default:
			this.cost = 0.00;
			break;
		}
		
	}
	
	public double getCost(){
		return this.cost;
	}

	public String getStrSize(){
		switch(this.size){
		case(1):
			return "Small";
		case(2):
			return "Medium";
		case(3):
			return "Large";
		default:
			return " ";
		}
	}
	
	public String toString(){
		return "Size: " + this.getStrSize() + ", Cost: " + usDollars.format(this.getCost());
	}
}
