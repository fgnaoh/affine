<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        table{
            width: 50%;
        }
        th, td{
            border: 1px solid black;
            padding: 8px;
        }
    </style>
</head>
<body>
    <h1>Table</h1>
    <?php
        $Products = array("001" => array("name"=> "apple","quantity"=>"200" ,"price"=>"20000"),
        "002" => array("name"=> "orange","quantity"=>"2070" ,"price"=>"30000"),
        "003" => array("name"=> "water melon","quantity"=>"400", "price"=>"40000"),
        "004" => array("name"=> "lemon","quantity"=>"2100" ,"price"=>"50000"),
        "005" => array("name"=> "pineapple","quantity"=>"2020", "price"=>"60000"));
        $total = 0;
    ?>
        <table >
        <tr>
            <th>Code</th>
            <th>Name</th>
            <th>Quantity</th>
            <th>Price</th>
        </tr>
        <?php
            foreach($Products as $key=> $value):
        ?>
        <tr>
            <td style><?php echo $key; ?></td>
            <td><?php echo $value['name']; ?></td>
            <td><?php echo $value['quantity']; ?></td>
            <td><?php echo $value['price']; ?></td>
        </tr>
        <?php
            $total += $value['quantity'] * $value['price'];
        ?>
        <?php 
            endforeach;
        ?>
        <tr>
            <td colspan="4">Total: <?php echo $total; ?></td>
        </tr>

    </table>
</body>
</html>
