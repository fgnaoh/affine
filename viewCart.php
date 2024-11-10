<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Xem giỏ hàng</title>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>
	<table class="table-striped" width="100%">
	<thead>
		<tr>
			<th>STT</th>
			<th>Mã hàng</th>
			<th>Tên hàng</th>
			<th>Số lượng</th>
			<th>Đơn giá</th>
			<th>Thành tiền</th>
		</tr>
	</thead> 
	<tbody>
		<?php
			//khởi động phiên
			session_start();
			//kiểm tra giỏ hàng đã tồn tại chưa
			if(isset($_SESSION['cart'])){
				$count = 0;
				$total = 0;
				//lấy giỏ hàng ra
				$cart = $_SESSION['cart'];
				foreach ($cart as $code => $item) {
					$count++;
					$total+=$item['quantity']*$item['price'];
			?>
				<tr>
					<td><?=$count?></td>
					<td><?=$code?></td>
					<td><?=$item['name']?></td>
					<td><?=$item['quantity']?></td>
					<td><?=$item['price']?></td>
					<td><?=$item['quantity']*$item['price']?></td>
				</tr>
			<?php
				}//end for
			}//end if
			if(isset($total)){
		?>
		<tr>
			<td colspan="5">Tổng tiền</td>
			<td><?=$total?></td>
		</tr>
		<?php
	}//end if kiểm tra tồn tại biến total
	?>
	</tbody>
	</table>
	<p style="text-align: right;">
		<a href="display.php"><button class="btn btn-success">Mua tiếp</button></a>
		<a href="orders.php"><button class="btn btn-primary">Đặt hàng</button></a>
	</p>
</body>
</html>