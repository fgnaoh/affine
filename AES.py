<!-- product_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Product Form</title>
</head>
<body>
    <h2>Nhập thông tin sản phẩm</h2>
    <form action="save_product.php" method="post" enctype="multipart/form-data">
        Mã hàng: <input type="text" name="ma_hang" required><br>
        Tên hàng: <input type="text" name="ten_hang" required><br>
        Nhóm hàng: 
        <select name="nhom_hang">
            <?php
            $lines = file('category.txt');
            foreach ($lines as $line) {
                list($ma_nhom, $ten_nhom) = explode("\t", trim($line));
                echo "<option value=\"$ma_nhom\">$ten_nhom</option>";
            }
            ?>
        </select><br>
        Số lượng: <input type="number" name="so_luong" required><br>
        Đơn giá: <input type="number" name="don_gia" required><br>
        Hình ảnh: <input type="file" name="hinh_anh" accept="image/*"><br>
        <input type="submit" value="Lưu sản phẩm">
    </form>
</body>
</html>
