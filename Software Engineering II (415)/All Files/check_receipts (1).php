<?php   
    session_start();
     if($_SESSION['logged'] == false){
        header("Location: login_page.html");
        exit;
    }
    if($_SESSION['type'] != 'Owner' && $_SESSION['type'] != 'Manager' && $_SESSION['type'] != 'Employee'){
        header("Location: main_page.html");
        exit;
    }
  @     $db = new mysqli('localhost','hulberb2_charley_smith','charleysmith12345','hulberb2_Users_Fall20_Sec1');

    
      if (mysqli_connect_errno()) {
         echo 'Error: Could not connect to database.  Please try again later.';
         exit;
      }
?>  
<!DOCTYPE html>
<html>
<head>
  <title>Nikki Dippy's - All Order Results</title>
</head>
<body>
<h1>Nikki Dippy's Graphics - All Order Results</h1>
<h2>Order Results</h2>
<?php
    $query = "select * from orders";
    $result = $db->query($query);
    $num_rows = $result->num_rows;
    for($i = 0; $i < $num_rows; $i++){
        $row = $result->fetch_assoc();
        echo $row['receipt']."<br/><br/>";

    }
    
    if($num_rows == 0){
        echo "There are no orders :(";
    }
    $db->close();
?>
</body>
</html>