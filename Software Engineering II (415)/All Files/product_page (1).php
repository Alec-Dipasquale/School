<?php
    session_start();
    if(isset($_POST['log_out'])) {
       $_SESSION['logged'] = false;
    }
    if($_SESSION['logged'] == false){
        header("Location: login_page.html");
    } else{
        $username = $_SESSION['username'];
    }
    @ $db = new mysqli('localhost','hulberb2_charley_smith','charleysmith12345','hulberb2_Users_Fall20_Sec1');

    
      if (mysqli_connect_errno()) {
         echo 'Error: Could not connect to database.  Please try again later.';
         exit;
      }
      if(isset($_POST['product_id'])){
        $query_product = "select * from products where product_id like '%".$_POST['product_id']."%'";
        $result = $db->query($query_product);
        $num_results = $result->num_rows;
        
      }
      if(isset($_POST['add_to_cart'])) {
            $quantity = $_POST['quantity'];
            $username = $_POST['username'];
            $product_id = $_POST['product_id'];
            
            if (!get_magic_quotes_gpc()) {
                $username = addslashes($username);
                $product_id = addslashes($product_id);
                $quantity = addslashes($quantity);
                }

            echo "<h1>";
            $update_cart_query = "update cart_items set quantity = '".$quantity."' where (product_id = '".$product_id."' AND username = '".$username."') ";
            $update_result= $db->query($update_cart_query);
            $check_rows_num= $db -> affected_rows;
            if ( $check_rows_num == 0) {
                
                $insert_cart_query = "insert into cart_items values (NULL, '".$username."', '".$product_id."', '".$quantity."')";
                $insert_cart_result = $db->query($insert_cart_query);
    
                if ($insert_cart_result) {
                    echo  $quantity." item placed in cart.</h1>";
                } else {
                  	echo "An error has occurred.  The item was not added to cart.";
                }
                
            } else{
                echo "Cart updated";
            }
            
            echo "</h1>";

            }
    
    ini_set('session.cache_limiter','public');
    session_cache_limiter(false);
    

?>
<html>
    <style>
        .card {
            max-width:90%;
            margin: auto;
            text-align: center;
            font-family: arial;
            overflow:hidden;
            padding-left: 15px;
            padding-right: 15px;
            line-height: 1.5;

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
    </style>

<body>
<h1>Product Page:</h1>

    
<div
    <form method="post" >
    <?php

        
             
              
            
                
        for ($i=0; $i <1; $i++) {
            $count++;
            if($count > $num_results){
                break;
            }
            $row = $result->fetch_assoc();
             
            echo '<div class="card">';
            echo '<p><strong>Product Number: ';
            $product_id= htmlspecialchars(stripslashes($row["product_id"]));
            echo $product_id;
            echo '<br/>Name: ';
            echo htmlspecialchars(stripslashes($row["name"]));
            echo '</strong><br/>';
            echo '<img src="data:image/jpg;base64,'.base64_encode( $row['img'] ).'" style="max-width:500px"/>';
            echo '<br/>Description: ';
            echo htmlspecialchars(stripslashes($row["description"]));
            echo '<br/>Price: $';
            echo htmlspecialchars(stripslashes($row["price"]));
            echo '<br/>In Stock: ';
            $in_stock= htmlspecialchars(stripslashes($row["quantity"]));
            echo $in_stock;
            
    }
    
?>
        <form method="post"> 
                <?php 
                echo '<input style="font-size:25px;width:5%" type="number" name="quantity" min=1 max ='.$in_stock.'>';
                echo '<input type="hidden" name="username" value='.$username.'>';
                echo '<input type="hidden" name="product_id" value= '.$product_id.'>';
                ?>
                <input style="width:13%;" type="submit" name="add_to_cart" value="Add To Cart"/> 
        </form> 
        <form method="post" action="main_page.php">
            <input style="width:20%" type="submit" name="home" value = "Home"/>
        </form>
            
            <?php
            
        
        $db->close();
        ?>
<br/></p>
</div>
</body>
</html>



