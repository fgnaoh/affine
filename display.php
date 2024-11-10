<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Hiển thị sản phẩm</title>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>
	<a href="viewCart.php"><button class="btn btn-primary">Xem giỏ hàng</button></a>
<table width="100%" class="table-striped">
	<caption>DANH SÁCH HÀNG HÓA</caption>
	<thead>
		<tr>
			<th>STT</th>
			<th>Mã hàng</th>
			<th>Tên hàng</th>
			<th>Số lượng</th>
			<th>Đơn giá</th>
			<th>Hình ảnh</th>
			<th>Chọn mua</th>
		</tr>
	</thead>
	<tbody>
		<?php
			//mở file để đọc
			$fh = fopen("hang.txt","r");
			$count = 0;
			//đọc lần lượt từng dòng của file. Mỗi dòng của file tương ứng một dòng của bảng
			while(!feof($fh)) {
				$line = fgets($fh);
				if(!empty($line)){
					$arr = explode("\t", $line);
					$count++;
			?>
			<tr>
				<td><?=$count?></td>
				<td><?=$arr[0]?></td>
				<td><?=$arr[1]?></td>
				<td><?=$arr[2]?></td>
				<td><?=$arr[3]?></td>
				<td>
					<img src="images/<?=$arr[4]?>" width="200px">
				</td>
				<td>
					<a href="addCart.php?code=<?=$arr[0]?>&name=<?=$arr[1]?>&price=<?=$arr[3]?>"><button class="btn btn-success">Mua</button></a>
				</td>
			</tr>
			<?php		
				}//end if
			}	//end while
			fclose($fh);
		?>
		<a href="hang.php">Back to Enter Product (hang.php)</a>
	</tbody>
	
</table>
</body>
</html>