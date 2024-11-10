<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Form nhập hàng</title>
</head>
<body>
	<form action="nhaphang.php" method="post" enctype="multipart/form-data">
	<label for="code">Mã hàng</label>
	<input type="text" id="code" name="code">
	<br>
	<label for="code">Tên hàng</label>
	<input type="text" id="name" name="name">

	<br>
	<label for="category">Nhóm hàng</label>
	<select id="category" name="category">
		<?php
			//Mở file category.txt để đọc
			$fh = fopen("category.txt","r");
			//Đọc lần lượt từng dòng, mỗi dòng tạo ra option
			while(!feof($fh)){//khi chưa kết thúc file
				//đọc ra từng dòng
				$line = fgets($fh);
				//kiểm tra nếu dòng không trống
				if(!empty($line)){
					$arr = explode("\t",$line);
					echo '<option value="'.$arr[0].'">'.$arr[1].'</option>';
				}

			}
			//đóng file lại
			fclose($fh);
		?>
	</select>
	<br>
	<label for="image">Ảnh của hảng</label>
	<input type="file" id="image" name="image">
	<br>
	<label for="quantity">Số lượng</label>
	<input type="text" id="quantity" name="quantity">
	<br>
	<label for="price">Đơn giá</label>
	<input type="text" id="price" name="price">
	<br>
	<button type="submit">Lưu</button>
	<button type="reset">Bỏ qua</button>
</form>
</body>
</html>