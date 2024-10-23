<?php
// view_products.php
session_start();

if (!isset($_SESSION['cart'])) {
    $_SESSION['cart'] = [];
}

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['add_to_cart'])) {
    $code = $_POST['code'];
    $name = $_POST['name'];
    $price = $_POST['price'];
    
    if (!isset($_SESSION['cart'][$code])) {
        $_SESSION['cart'][$code] = ['name' => $name, 'quantity' => 1, 'price' => $price];
    } else {
        $_SESSION['cart'][$code]['quantity']++;
    }
    echo "Added in cart";
}

$products = file('hang.txt');
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Products</title>
</head>
<body>
    <h2>Product's list</h2>
    <table border="1">
        <tr>
            <th>code</th>
            <th>name</th>
            <th>price</th>
            <th>classify</th>
        </tr>
        <?php foreach ($products as $product): ?>
            <?php list($code, $name, , , $price) = explode("\t", trim($product)); ?>
            <tr>
                <td><?= $code ?></td>
                <td><?= $name ?></td>
                <td><?= $price ?></td>
                <td>
                    <form method="post">
                        <input type="hidden" name="code" value="<?= $code ?>">
                        <input type="hidden" name="name" value="<?= $name ?>">
                        <input type="hidden" name="price" value="<?= $price ?>">
                        <input type="submit" name="add_to_cart" value="Buy">
                    </form>
                </td>
            </tr>
        <?php endforeach; ?>
    </table>
    <a href="view_cart.php">Cart</a>
</body>
</html>