<?php
// save_product.php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $ma_hang = $_POST['ma_hang'];
    $ten_hang = $_POST['ten_hang'];
    $nhom_hang = $_POST['nhom_hang'];
    $so_luong = $_POST['so_luong'];
    $don_gia = $_POST['don_gia'];
    $hinh_anh = $_FILES['hinh_anh']['name'];

    move_uploaded_file($_FILES['hinh_anh']['tmp_name'], "uploads/$hinh_anh");

    $data = "$ma_hang\t$ten_hang\t$nhom_hang\t$so_luong\t$don_gia\t$hinh_anh\n";
    file_put_contents('hang.txt', $data, FILE_APPEND);

    echo "Sản phẩm đã được lưu.";
}
?>
