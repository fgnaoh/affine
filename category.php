<?php
	//lấy dữ liệu từ form gửi lên
	$code = $_POST['code'];
	$name = $_POST['name'];
	$desc = $_POST['description'];
	//Mở file để ghi bổ sung
	$fh = fopen("category.txt","a");
	fputs($fh,$code."\t".$name."\t".$desc."\n");
	fclose($fh);
	header("Location: category.html");
?>