<?php
// save_product.php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $code = $_POST['code'];
    $name = $_POST['name'];
    $class = $_POST['class'];
    $quantity = $_POST['quantity'];
    $price = $_POST['price'];
    $image = $_FILES['image']['name'];

    move_uploaded_file($_FILES['image']['tmp_name'], "uploads/$image");

    $data = "$code\t$name\t$classify\t$quantity\t$price\t$image\n";
    file_put_contents('hang.txt', $data, FILE_APPEND);

    echo "Product was saved :))";
}
?>