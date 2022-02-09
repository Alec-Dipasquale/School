<?php
    session_start();
    if($_SESSION['logged'] == false){
        header("Location: login_page.html");
    } else{
        $username = $_SESSION['username'];
    }
    @    $db = new mysqli('localhost','hulberb2_charley_smith','charleysmith12345','hulberb2_Users_Fall20_Sec1');

    
      if (mysqli_connect_errno()) {
         echo 'Error: Could not connect to database.  Please try again later.';
         exit;
      }
      
      if(isset($_POST['delete'])){
        $query_cart_item_delete = "delete from cart_items where cart_item_id = ".$_POST['cart_item_id'];
        $delete_result= $db->query($query_cart_item_delete);
        if($delete_result){
            echo "<p>Item deleted from cart</p>";
        } else{
            echo "<p>Error deleting from cart</p>";
        }
    }
    
    
    $query_for_cart = "select * from cart_items where username = '".$username."'";
    $result = $db->query($query_for_cart);
    $num_results = $result->num_rows;
    

?>
<html>
    <style>
        table, th, td {
          border: 1px solid black;
          text-align: center;
          min-width: 100px;
        }
        input[type=submit]{
            border: 1 solid white;
            outline: 0;
            padding: 12px;
            color: white;
            background-color: #000;
            text-align: center;
            cursor: pointer;
            font-size: 18px;
        }
        .container {
          max-height: 300px;
        }
        .center {
          margin: 0;
          position: absolute;
          top: 50%;
          left: 50%;
          -ms-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
        }
        .vertical-center {
          margin: 0;
          position: absolute;
          top: 50%;
          -ms-transform: translateY(-50%);
          transform: translateY(-50%);
        }
        .card {
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            max-width: 750px;
            margin: auto;
            text-align: center;
            font-family: arial;
            overflow:hidden;
            white-space: nowrap;
            padding: 15px;
            line-height: 1.5;

        }
    </style>

<body>
    <h1 style="text-align:center;">Your Cart</h1>
    
<div class="card">
    
    <table>
            <thead>
                <tr>
                    <td colspan="2">Product</td>
                    <td>Price</td>
                    <td>Quantity</td>
                    <td>Total</td>
                </tr>
                </thead>
            <tbody>
                
               <?php
                $query = "select * from cart_items where username = '".$username."'";
                $result = $db->query($query);
                $num_results = $result->num_rows;
                $subtotal = 0;
                $total = 0;
                for ($i=0; $i <$num_results; $i++) {
                    $row = $result->fetch_assoc();
                    $product_query = "SELECT * FROM products WHERE product_id like '%".stripslashes($row['product_id'])."%'";
                    $product = $db->query($product_query);
                    for($j = 0; $j <  1;$j++){
                        $product_row = $product->fetch_assoc();
                        $item_price = $product_row['price'];
                        $item_quantity = $row['quantity'];
                        $item_total=$item_price * $item_quantity;
                        $subtotal = $subtotal + $item_total;
                        
                        echo "<tr><td><img src='data:image/jpg;base64,".base64_encode( $product_row["img"] )."' style='max-width:100px;'/></td>";
                        echo "<td>".$product_row['name']."</td>";
                        echo "<td>$".$item_price."</td>";
                        echo "<td><a>".$item_quantity."</a></td>";
                        echo "<td>$".$item_total."</td>";
                        echo "<td style='border:0px;'><form method='post'>
                        <input type='hidden' name='cart_item_id' value='".htmlspecialchars(stripslashes($row['cart_item_id']))."'/>
                        <input type='submit' name='delete' value= 'remove'/></form></td>";
                        echo "</tr>";
                    }
                }
                $tax_rate = .07;
                echo "<td colspan ='4'>subtotal</td><td>".$subtotal."</td></tr>";
                $tax = number_format($subtotal * $tax_rate,2);
                echo "<td colspan ='4'>tax</td><td>".$tax."</td></tr>";
                $total = number_format($subtotal + $tax,2);
                echo "<td colspan ='4'>total</td><td>".$total;
               ?>
</td></tr></table>
        <form action = 'receipt.php' method='post'>
            <div style="text-align:right;">
                <?php
                    echo "<input type='hidden'  name='username' value='".$username."'/>";
                ?>
                <input style="width:20%"type="submit" name="check_out" value = "check out"/>
            </div>
        </form>
            
            <?php
            
                
                $db->close();
            ?>
        
</div>

                <div style="text-align:center;padding-top:25px;">
                <form method="post" action="main_page.php">
                <input style="width:20%" type="submit" name="home" value = "Home"/>
                </div>
</body>
</html>