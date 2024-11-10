<?php
	//lưu các hàng trong giỏ vào trong file. Mỗi hàng lưu trên một dòng. Mỗi thông tin của hàng sẽ cách nhau 8 khoảng trắng.
	//giỏ hàng lưu trong phiên
	//khởi động phiên làm việc
	session_start();
	//lấy ra giỏ hàng
	$shc = $_SESSION['cart'];
	if(isset($_SESSION['no'])){
		$no = $_SESSION['no'];
	}
	else{
		$no = 0;
	}
	$no++;
	$_SESSION['no'] = $no;
	//Mở file donhang.txt để ghi thông tin hóa đơn
	$fh = fopen("donhang.txt","a");
	//tính tổng tiền
	$total = 0;
	foreach ($shc as $code => $item) {
		$total+=$item['quantity']*$item['price'];
	}
	
	$line = $no."\t". date("d/m/Y H:i:s")."\t".$total."\n";
	//ghi vào file
	fputs($fh,$line);
	//Đóng file lại
	fclose($fh);
	//Mở file chi tiết đơn hàng
	$fh = fopen("chitiet.txt","a");
	foreach ($shc as $code => $item) {
		$inf = $no."\t".$code."\t".$item['name']."\t".$item['quantity']."\t".$item['price']."\n";
		fwrite($fh,$inf);
	}
	fclose($fh);

	//xóa giỏ hàng
	unset($_SESSION['cart']);
	//Trở về trang mua hàng
	header("Location:listOrders.php");
?>