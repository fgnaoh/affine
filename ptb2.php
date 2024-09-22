<?php
    //lay du lieu tu form gui len
    $a = $_POST['a'];
    $b = $_POST['b'];
    $c = $_POST['c'];
    //tinh delta
    $delta = $b*$b - 4*$a*$c;
    if($delta<0){
        echo "Phuong trinh co 2 nghiem phuc";
        $x1 = "(-$b-".sqrt(-$delta)."*i)/".(2*$a);
        $x2 = "(-$b+".sqrt(-$delta)."*i)/".(2*$a);
        echo "<br>x1 = $x1";
        echo "<br>x2 = $x2";
    } 
    else if($delta==0){
        $x = -$b/(2*$a);
        echo "Phuong trinh co nghiem kep x1 = x2 = $x";
    }
    else{
        echo "Phuong trinh co 2 nghiem thuc phan biet";
        $x1 = (-$b-sqrt($delta))/(2*$a);
        $x2 = (-$b+sqrt($delta))/(2*$a);
        echo "<br>x1 = $x1, x2 = $x2";
    }
    echo '<br><a href="ptb2.html">Back</a>';
?>