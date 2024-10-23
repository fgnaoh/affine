<?php
// view_products.php
session_start();

if (!isset($_SESSION['cart'])) {
    $_SESSION['cart'] = [];
}

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['add_to_cart'])) {
    $ma_hang = $_POST['ma_hang'];
    $ten_hang = $_POST['ten_hang'];
    $don_gia = $_POST['don_gia'];
    
    if (!isset($_SESSION['cart'][$ma_hang])) {
        $_SESSION['cart'][$ma_hang] = ['ten_hang' => $ten_hang, 'so_luong' => 1, 'don_gia' => $don_gia];
    } else {
        $_SESSION['cart'][$ma_hang]['so_luong']++;
    }
    echo "Đã thêm vào giỏ hàng.";
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
    <h2>Danh sách sản phẩm</h2>
    <table border="1">
        <tr>
            <th>Mã hàng</th>
            <th>Tên hàng</th>
            <th>Đơn giá</th>
            <th>Hành động</th>
        </tr>
        <?php foreach ($products as $product): ?>
            <?php list($ma_hang, $ten_hang, , , $don_gia) = explode("\t", trim($product)); ?>
            <tr>
                <td><?= $ma_hang ?></td>
                <td><?= $ten_hang ?></td>
                <td><?= $don_gia ?></td>
                <td>
                    <form method="post">
                        <input type="hidden" name="ma_hang" value="<?= $ma_hang ?>">
                        <input type="hidden" name="ten_hang" value="<?= $ten_hang ?>">
                        <input type="hidden" name="don_gia" value="<?= $don_gia ?>">
                        <input type="submit" name="add_to_cart" value="Mua">
                    </form>
                </td>
            </tr>
        <?php endforeach; ?>
    </table>
    <a href="view_cart.php">Giỏ hàng</a>
</body>
</html>
