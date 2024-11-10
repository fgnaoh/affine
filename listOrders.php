<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Danh sách đơn hàng</title>
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
			<th>Mã đơn hàng</th>
			<th>Thời gian</th>
			<th>Tổng tiền</th>
			<th>Xem chi tiết</th>
		</tr>
	</thead>
	<tbody>
		<?php
			//Mở file donhang.txt để đọc
			$fh = fopen("donhang.txt","r");
			$count = 0;
			while(!feof($fh)){
				$line = fgets($fh);
				if(!empty($line)){
					$arr = explode("\t",$line);
					$count++;
			?>
			<tr>
				<td><?=$count?></td>
				<td><?=$arr[0]?></td>
				<td><?=$arr[1]?></td>
				<td><?=$arr[2]?></td>
				<td>
					<a href="showDetails.php?no=<?=$arr[0]?>"><button class="btn btn-primary">Xem chi tiết</button></a>
				</td>
			</tr>
			<?php		
					
				}//end if
			}//end while
			fclose($fh);
		?>
	</tbody>
</table>
<a href="display.php"><button class="btn btn-success">Back</button></a>
</body>
</html>