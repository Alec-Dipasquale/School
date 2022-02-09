import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.FlowPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.stage.Stage;

public class PizzaUI extends Application{
	Order pizzaOrder = new Order();
	
	@Override
	public void start(Stage primaryStage){
		
		
		//Label Order Pizza here, Font: Arial, Size: 20, Color:Red
		Label lblPizza = new Label("Order Pizza Here");
		lblPizza.setTextFill(Color.RED);
		lblPizza.setFont(new Font ("Arial", 20));
		
		//label and radio buttons for sizes
		Label lblSize = new Label("Size");
		RadioButton rbSmall = new RadioButton("Small");
		RadioButton rbMedium = new RadioButton("Medium");
		RadioButton rbLarge = new RadioButton("Large");
		
		//Group Radio Buttons for sizes
		ToggleGroup groupSize = new ToggleGroup();
		rbSmall.setToggleGroup(groupSize);
		rbMedium.setToggleGroup(groupSize);
		rbLarge.setToggleGroup(groupSize);
		rbMedium.setSelected(true);
		
		//HBox to hold radio Buttons
		HBox hboxSizes = new HBox(10);
		hboxSizes.getChildren().addAll(rbSmall, rbMedium, rbLarge);

		//label and Check buttons for toppings
		Label lblToppings = new Label("Toppings: ");
		CheckBox cbCheese = new CheckBox("Cheese");
		cbCheese.setSelected(true);
		//Meats
		Label lblMeats = new Label("Meats: ");
		CheckBox cbPepperoni = new CheckBox("Pepperoni");
		CheckBox cbSausage = new CheckBox("Sausage");
		CheckBox cbHam = new CheckBox("Ham");
		CheckBox cbChicken = new CheckBox("Chicken");
		CheckBox cbBeef = new CheckBox("Beef");
		//vegetables & fruit
		Label lblVeg = new Label("Veggies and fruit: ");
		CheckBox cbYellowPep = new CheckBox("Yellow Peppers");
		CheckBox cbBellPep = new CheckBox("Bell Peppers");
		CheckBox cbBroccoli = new CheckBox("Broccoli");
		CheckBox cbPineapple = new CheckBox("Pineapple");



		//boxes for Toppings
		VBox vboxMeats = new VBox(10);
		vboxMeats.getChildren().addAll(lblMeats, cbPepperoni, cbSausage, cbHam, cbChicken, cbBeef);
		VBox vboxVeg = new VBox(10);
		vboxVeg.getChildren().addAll(lblVeg, cbBellPep, cbYellowPep, cbBroccoli, cbPineapple);
		HBox hboxToppings = new HBox(20);
		hboxToppings.getChildren().addAll(vboxMeats, vboxVeg);


		//Button that adds Pizza to order 
		Button btnAddPizza = new Button("Add Pizza to Order");
		
		//VBox pane to hold Pizza Label, Size Label, Radio Buttons, Add Pizza Button
		VBox vboxL = new VBox(15);
		vboxL.getChildren().addAll(lblPizza, lblSize, hboxSizes, lblToppings, cbCheese, hboxToppings, btnAddPizza);

		//VLabel for right side as header for order
		Label lblOrder = new Label("Your Order");
		lblOrder.setTextFill(Color.PURPLE);
		lblOrder.setFont(new Font("Arial", 20));
		
		//Text area that displays order
		TextArea taOrder = new TextArea();
		taOrder.setPrefColumnCount(20);
		taOrder.setPrefRowCount(20);
		
		//VBox to hold label and text area
		VBox vboxR = new VBox(15);
		vboxR.getChildren().addAll(lblOrder,taOrder);
		
		//FlowPane to hold final order button centered
		FlowPane pBottom = new FlowPane();
		Button btnPlOrder = new Button("Place Order");
		pBottom.getChildren().add(btnPlOrder);
		pBottom.setAlignment(Pos.BASELINE_CENTER);
		
		//BorderPane to hold all controls nested in other panes
		BorderPane pane = new BorderPane();
		pane.setPadding(new Insets(10,10,10,10));
		pane.setLeft(vboxL);
		pane.setRight(vboxR);
		pane.setBottom(pBottom);
		
		//Set scene and primary stage
		Scene scene = new Scene(pane, 500, 500);
		primaryStage.setTitle("Pizza Shop");
		primaryStage.setScene(scene);
		primaryStage.show();
		
		
		
		//////////////////////////////////////////////////////////////////////////////////////
		btnAddPizza.setOnAction(e ->{
			if(rbSmall.isSelected()){
				pizzaOrder.addPizza(new Pizza(1));
			}
			else if(rbMedium.isSelected()){
				pizzaOrder.addPizza(new Pizza(2));

			}
			else if(rbLarge.isSelected()){
				pizzaOrder.addPizza(new Pizza(3));
			}
			if (cbPepperoni.isSelected()) pizzaOrder.addToppings(new Toppings("Pepperoni"));
			if (cbBeef.isSelected()) pizzaOrder.addToppings(new Toppings("Beef"));
			if (cbChicken.isSelected()) pizzaOrder.addToppings(new Toppings("Chicken"));
			if (cbHam.isSelected()) pizzaOrder.addToppings(new Toppings("Ham"));
			if (cbSausage.isSelected()) pizzaOrder.addToppings(new Toppings("Sausage"));
			if (cbBellPep.isSelected()) pizzaOrder.addToppings(new Toppings("Bell Peppers"));
			if (cbBroccoli.isSelected()) pizzaOrder.addToppings(new Toppings("Broccoli"));
			if (cbPineapple.isSelected()) pizzaOrder.addToppings(new Toppings("Pineapple"));
			if (cbYellowPep.isSelected()) pizzaOrder.addToppings(new Toppings("Yellow Peppers"));

			taOrder.setText(pizzaOrder.toString());
		});
		////////////////////////////////////////////////////////////////////////////////////////


		////////////////////////////////////////////////////////////////////////////////////////
		btnPlOrder.setOnAction(e-> {
			taOrder.setText(pizzaOrder.finalBill());
		});
		////////////////////////////////////////////////////////////////////////////////////////
		
	}
	
	
	public static void main(String[] args){ launch(args);	}

}
