<?php   
    session_start();
  @     $db = new mysqli('localhost','hulberb2_charley_smith','charleysmith12345','hulberb2_Users_Fall20_Sec1');

    
      if (mysqli_connect_errno()) {
         echo 'Error: Could not connect to database.  Please try again later.';
         exit;
      }
     if(isset($_POST['log_out'])) {
       $_SESSION['logged'] = false;
    }
    session_start();
    if($_SESSION['logged'] == false){
        header("Location: login_page.html");
    } else{
        $username = $_SESSION['username'];
    }
?>  
<!DOCTYPE html>
<html>

<head>
     
    <style>
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
        button {
            border: 1 solid white;
            outline: 0;
            padding: 12px;
            color: white;
            background-color: #000;
            text-align: center;
            cursor: pointer;
            width: 100%;
            font-size: 18px;
        }
        .title{
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            margin: auto;
            text-align: center;
            font-family: arial;
            overflow:hidden;
            width: 70%;
            padding-left: 15px;
            padding-right: 15px;
            line-height: 1.5;
        }
        .results{
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            margin: auto;
            text-align: center;
            font-family: arial;
            overflow:hidden;
            white-space: nowrap;
            width: 30%;
            padding: 15px;
            line-height: 1.5;
        }
        .card {
            
            padding-left: 15px;
            padding-right: 15px;
            text-align: center;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            width: 350px;
            margin: auto;
            overflow:hidden;
            padding-left: 15px;
            padding-right: 15px;
            line-height: 1.5;

        }
        
        .price {
            color: grey;
        }
        
        .card button {
            
            padding: 12px;
            border: 1 solid white;
            outline: 0;
            color: white;
            background-color: #000;
            text-align: center;
            cursor: pointer;
            width: 100%;
            font-size: 18px;
        }
        
        .card button:hover {
            opacity: 0.5;
        }
        .table_style {
            display: inline-block;
            margin:  auto;
            padding: 10px;
            
        }
        .outer_table_style {
            width: 100%;
            text-align: center;
            
        }
        img {
            border-radius: 10px;
            width: 100%;
        }
    </style>
    <title>Main Page</title>
</head>


<body>
    <div class= "title">
        <h1 >Nikki Dippy's Catalog</h1>
        <p>This is a catalog of all of Nikki's current products.</p>
        <form method="post" >
            <input style="width: 100%;" type="submit" name="log_out" value = "Log Out"/></form>
    </div>
    
    
    <?php
    if($_SESSION['type'] == "Owner" || $_SESSION['type'] == 'Manager' ||$_SESSION['type'] == 'Employee'){
            echo '<div style = "border:1px solid black; padding: 5px;">';
            echo '<h1>Admin Section</h1>';
            echo '<form method="post" action="check_receipts.php">
            <input style="width: 100%;" type="submit" name="check_all_orders" value = "Check All Orders"/></form>';  
            
            if($_SESSION['type'] == "Owner" || $_SESSION['type'] == 'Manager'){
                echo '<a href="insert.html" style="padding: 5px;">
                <button type="submit">Insert Product</button>
                </a>';
                
                if($_SESSION['type'] == "Owner"){
                    echo '<a href="delete_product.html" style="padding: 5px;">
                    <button type="submit">Delete Product</button>
                    </a></div>'; 
                }
            }
    }
    if(isset($_POST['search']) && isset($_POST['searchterm'])) {
        $searchterm = $_POST['searchterm'];
        $query = "select * from products 
        where (product_id like '%".$searchterm."%' OR 
        name like '%".$searchterm."%' OR 
        description like '%".$searchterm."%')";
    } else {
        $query = "select * from products";
    }
    if(isset($_POST['show_all'])) {
        $query = "select * from products";
    }
     
    
    
    $result = $db->query($query);
    
    $num_results = $result->num_rows;
    echo '<div class= "results">';
    echo "<p>Number of products found: ".$num_results."</p>";
    echo '<form method = "post" action ="cart.php">
            <input style="width:100%;"  type = "submit" name = "go_to_cart" value ="Cart"/></form>
            <form method="post" action="main_page.php">
            <input style="width:100%;" type="submit" name="show_all" value = "Full Catalog"/></form>';
    echo '</div>';
    echo '<div class= "results">';
    echo "<form method='post' action='main_page.php'>
                    <input type='text' name='searchterm' />
                    <input type='submit' name='search' value = 'search'/>
                </form>";
    echo '</div>';
    echo '<div class= "outer_table_style"><div class= "table_style">';
    echo '<p>';
    echo '<table style="">';
    $count = 0;
    for ($i=0; $i <($num_results/3); $i++) {
        echo '<tr>';
        for($j=0; $j <3; $j++){
            $count++;
            if($count > $num_results){
                break;
            }
            $row = $result->fetch_assoc();
             
            echo '<td><div class="card">';
            echo '<p><strong>Product Number: ';
            echo htmlspecialchars(stripslashes($row["product_id"]));
            echo '<br/>Name: ';
            echo htmlspecialchars(stripslashes($row["name"]));
            echo '</strong><br/>';
            ini_set('memory_limit', '-1');
            echo '<img src="data:image/jpg;base64,'.base64_encode( $row['img'] ).'"/>';
            echo '<br/>Price: $';
            echo htmlspecialchars(stripslashes($row["price"]));
            echo '<br/>In Stock: ';
            echo htmlspecialchars(stripslashes($row["quantity"]));
            echo '<br/></p>';
            echo '<form action="product_page.php" method="post">';
            echo '<input type = "hidden" name = "product_id" value = "'.htmlspecialchars(stripslashes($row["product_id"])).'" />';
            echo '<input type = "hidden" name = "username" value = "'.$username.'" />';
            echo '<p><button type="submit">See Product</button></p></form></div></td>';
            
        }
        echo '</tr>';
    }
    echo'</table></p></div></div>';
    ?>
    
    
    
    
    
    
    
        <?php
                          
       
        
        $db->close();
      

                          ?> 
    
    
    </body>
</html>