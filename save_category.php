<?php 
    if($_SERVER["REQUEST_METHOD"] == "POST"){
        $codeGroup = $_POST["codeGroup"];
        $nameGroup = $_POST["nameGroup"];
        $describeGroup = $_POST["describeGroup"];
        $data = "$codeGroup\t$nameGroup|$describeGroup\n";
        file_put_contents("category.txt",$data,FILE_APPEND);
        echo "Saved ;))";
    }
?>