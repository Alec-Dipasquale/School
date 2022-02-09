<?php

    session_start();

    $username=$_POST['username'];  
    $password=$_POST['password'];
    
    if (!$username || !$password) {     
        echo 'You have not entered credentials.';     
    exit;  } 
    
    //Connect to DB
    $db = new mysqli('localhost','hulberb2_charley_smith','charleysmith12345','hulberb2_Users_Fall20_Sec1');

    if (mysqli_connect_errno()) {    
        echo 'Error: Could not connect to database.  Please try again later.';exit;}

    //protect sql injections
    $username  = stripslashes($username);    
    $password = stripslashes($password);
    $username = mysqli_real_escape_string($db, $username);
    $password = mysqli_real_escape_string($db, $password);
    
    //$password = md5($password);
    
    $result = mysqli_query($db, "SELECT user_type FROM user_types WHERE username = '$username' and password = '$password'") or die("Failed to query.");
    $row = mysqli_num_rows($result);
    $type = $result->fetch_object();
    if($row == 1){
        
        $_SESSION["logged"] = true;
        $_SESSION["username"] = $username;
        $_SESSION["type"] = $type->user_type;


        header("Location: main_page.php");

    }
    else {
 
        echo "Failure to login!";

    }
    
    $result->free();    
    $db->close();

?>