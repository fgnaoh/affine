<?php
	//thêm hàng vào giỏ
	//Sử dụng phiên để lưu giỏ hàng
	session_start();//khởi đồng phiên lên
	//kiểm tra xem đã có giỏ hàng chưa
	if(isset($_SESSION['cart'])){//đã có giỏ hàng
		//lấy ra
		$cart = $_SESSION['cart'];
	}
	else{//chưa có thì tạo
		$cart = [];

	}
	//Lấy thông tin của hàng
	$code = $_GET['code'];
	$name = $_GET['name'];
	$price = $_GET['price'];
	//Kiểm tra xem hàng đã có trong giỏ chưa
	//[code=>[name=>abc,quantity=>2,price=>5000],...]
	if(array_key_exists($code, $cart)){//hàng đã có -->tăng số lượng lên 1(cart là biến và code là key)
		$cart[$code]['quantity']++;

	}
	else{//hàng chưa có trong giỏ
		$cart[$code] = array('name'=>$name ,'quantity'=>1,'price'=>$price);

	}
	//cập nhật phiên để lưu giỏ hàng hiện tại
	$_SESSION['cart'] = $cart;
	header("Location:viewCart.php");
?>