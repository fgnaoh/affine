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
        $total += $item['so_luong'] * $item['don_gia'];
        $detail = "$order_id\t$ma_hang\t{$item['ten_hang']}\t{$item['so_luong']}\t{$item['don_gia']}\n";
        file_put_contents('chitietdonhang.txt', $detail, FILE_APPEND);
    }

    $order = "$order_id\t$time\t$total\n";
    file_put_contents('donhang.txt', $order, FILE_APPEND);

    $_SESSION['cart'] = []; // Clear cart
    echo "Đơn hàng đã được đặt.";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Giỏ hàng</title>
</head>
<body>
    <h2>Giỏ hàng của bạn</h2>
    <table border="1">
        <tr>
            <th>Mã hàng</th>
            <th>Tên hàng</th>
            <th>Số lượng</th>
            <th>Đơn giá</th>
        </tr>
        <?php foreach ($_SESSION['cart'] as $ma_hang => $item): ?>
            <tr>
                <td><?= $ma_hang ?></td>
                <td><?= $item['ten_hang'] ?></td>
                <td><?= $item['so_luong'] ?></td>
                <td><?= $item['don_gia'] ?></td>
            </tr>
        <?php endforeach; ?>
    </table>
    <form method="post">
        <input type="submit" name="place_order" value="Đặt hàng">
    </form>
</body>
</html>
