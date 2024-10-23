<?php
// view_cart.php
session_start();

if (!isset($_SESSION['cart'])) {
    $_SESSION['cart'] = [];
}

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['place_order'])) {
    $order_id = file_exists('donhang.txt') ? count(file('donhang.txt')) + 1 : 1;
    $time = date('Y-m-d H:i:s');
    $total = 0;
    
    foreach ($_SESSION['cart'] as $ma_hang => $item) {
        $total += $item['quantity'] * $item['price'];
        $detail = "$order_id\t$code\t{$item['name']}\t{$item['quantity']}\t{$item['price']}\n";
        file_put_contents('chitietdonhang.txt', $detail, FILE_APPEND);
    }

    $order = "$order_id\t$time\t$total\n";
    file_put_contents('donhang.txt', $order, FILE_APPEND);

    $_SESSION['cart'] = []; // Clear cart
    echo "Clear cart.";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Giỏ hàng</title>
</head>
<body>
    <h2>Your Cart</h2>
    <table border="1">
        <tr>
            <th>Code</th>
            <th>Name</th>
            <th>Quantity</th>
            <th>Price</th>
        </tr>
        <?php foreach ($_SESSION['cart'] as $code => $item): ?>
            <tr>
                <td><?= $code ?></td>
                <td><?= $item['name'] ?></td>
                <td><?= $item['quantity'] ?></td>
                <td><?= $item['price'] ?></td>
            </tr>
        <?php endforeach; ?>
    </table>
    <form method="post">
        <input type="submit" name="place_order" value="Đặt hàng">
    </form>
</body>
</html>