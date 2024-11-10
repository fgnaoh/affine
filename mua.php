<?php
	session_start();//Khởi động session mới sử dụng được
	$shc = array();
	if(!isset($_SESSION['cart'])){//giỏ hàng chưa có
		$_SESSION['cart'] = $shc;
	}
	else{//nếu có rồi thì phải lấy giỏ hàng ra
		$shc = $_SESSION['cart'];
	}
	$code = $_POST['code'];
	$name = $_POST['name'];
	$quantity = $_POST['quantity'];
	$price = $_POST['price'];
	$path = "images/";
	$filename = $path.basename($_FILES['image']['name']);
	if(!file_exists($filename)){//file chưa có mới di chuyển từ thư mục temp vào thư mục mong muốn
		move_uploaded_file($_FILES['image']['tmp_name'], $filename);

	}
	/*//Kiểm tra trong mảng shc đã có hàng có mã như $code
	if(array_key_exists($code, $shc)){//tồn tại rồi cộng số lương lên $quantity
		$shc[$code]['quantity'] = $shc[$code]['quantity'] + $quantity;
	}
	else{//hàng chưa có trong giỏ
		$shc[$code]=array("name"=>$name,"quantity"=>$quantity,"price"=>$price);
	}
	//cập nhật lại giỏ hàng
		$_SESSION['cart'] = $shc;
		*/
	?>
		<table width="800px" align="center" border="1" style="border-collapse:collapse" cellpadding="5px">
			<caption>DANH SÁCH HÀNG ĐÃ MUA</caption>
			<thead>
				<tr>
					<th>No.</th>
					<th>Code</th>
					<th>Name</th>
					<th>Quantity</th>
					<th>Price</th>
					<th>Subtotal</th>
				</tr>
			</thead>
			<tbody>
				
				
<?php
		$count = 0;
		$total = 0;
		foreach($shc as $code=>$arr){
			$count++;
			$total+=$arr["quantity"]*$arr["price"];
?>
		<tr>
			<td align="center"><?=$count?></td>
			<td align="center"><?=$code?></td>
			<td><?=$arr["name"]?></td>
			<td align="right"><?=$arr["quantity"]?></td>
			<td align="right"><?=$arr["price"]?></td>
			<td align="right"><?=$arr["quantity"]*$arr["price"]?></td>
			
		</tr>
<?php	
	}//end for				
?>
	<tr>
		<td colspan="5" align="right"><b>Total</b></td>
		<td align="right"><?=$total?></td>
	</tr>
	<tr>
		<td colspan="6" align="right">
			<a href="hang.html"><button type="button">Mua tiếp</button></a>
			<a href="orders.php"><button type="button">Đặt hàng</button>
		</td>
	</tr>
	</tbody>
	</table>