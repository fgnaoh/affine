<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Xem chi tiết hóa đơn</title>
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
			//Lấy thông tin số hóa đơn
			$no = $_GET['no'];
			//Mở file chi tiết để đọc
			$fh = fopen("chitiet.txt","r");
			$count = 0;
			$total = 0;
			while(!feof($fh)){
				$line = fgets($fh);
				if(!empty($line)){
					$arr = explode("\t", $line);
					if($arr[0]==$no){
						$count++;
						$total+=floatval($arr[3])*floatval($arr[4]);
					?>
					<tr>
					<td><?=$count?></td>
					<td><?=$arr[1]?></td>
					<td><?=$arr[2]?></td>
					<td><?=$arr[3]?></td>
					<td><?=$arr[4]?></td>
					<td><?=floatval($arr[3])*floatval($arr[4])?></td>
				</tr>
					<?php	
					}//end if trung mã hóa đơn
				}	//end if dòng khác rỗng
				
			}//end while
			//đóng file
			fclose($fh);
			?>
			<tr>
			<td colspan="5">Tổng tiền</td>
			<td><?=$total?></td>
		</tr>

	</tbody>
	</table>
	<a href="listOrders.php"><button class="btn btn-success">Back</button></a>
</body>
</html>