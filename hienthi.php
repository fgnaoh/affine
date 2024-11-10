<?php
	//đọc từ file chi tiết để hiện ra màn hình. Mỗi hàng trên 1 dòng: mã hàng, tên hàng, số lượng, đơn giá, thành tiền
	//1. Mở file để đọc
	$fh = fopen("chitiet.txt","r");
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
		while(!feof($fh)){
			$line = fgets($fh);
			if($line!=""){
			$temp = explode("\t", $line);//[code,name,quantity,price]
			$total+=floatval($temp[2])*floatval($temp[3]);
			$count++;
			echo "<tr>";
			echo "<td align=\"center\">$count</td>";
			echo "<td>$temp[0]</td>";
			echo "<td>$temp[1]</td>";
			echo "<td align=\"right\">$temp[2]</td>";
			echo "<td align=\"right\">$temp[3]</td>";
			echo "<td align=\"right\">".floatval($temp[2])*floatval($temp[3])."</td>";
			echo "</tr>";	
		}//end if

		}//end while				
?>
	<tr>
		<td colspan="5" align="right"><b>Total</b></td>
		<td align="right"><?=$total?></td>
	</tr>
	<tr>
		<td colspan="6" align="right">
			<a href="hang.html"><button type="button">Mua tiếp</button></a>
			
		</td>
	</tr>
	</tbody>
	</table>