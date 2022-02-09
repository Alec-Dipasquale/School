<!DOCTYPE html>
<?php
session_start();
require_once('generic_fns.php');
permission();
?>
<html>

<head>
    <title>Admin</title>
    <style>
        #loginLabel {
            font-family: arial;
        }
        
        #admincommands {
            max-width: 700px;
            padding-top: 40px;
            padding-left: 15px;
            padding-right: 15px;
            text-align: center;
            margin: auto;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        }
        
        #loginBtn:hover {
            font-family: arial;
        }
    </style>
</head>



<body>

    <div id="admincommands">
        <form action="add_product.php" method="post">
            <h1>Admin</h1>

            <div style="text-align:center; padding:5px;" id="AddProduct">
                <input type="submit" name="addproduct" value="Add Product">
            </div>
			<div style="text-align:center; padding:5px;" id="ViewOrders">
				<input type="submit" name="vieworders" value="View Orders">
			</div>
			<div style="text-align:center;" id="ViewUsers">
                <input type="submit" name="viewusers" value="View Users">
            </div>		
        </form>
    </div>
</body>

</html>